import cv2
import torch
import numpy as np
import datetime as dt
from time import perf_counter


class DepthScanner(object):
    def __init__(self, camera:int=0, mode:str="standard", scale:float=1):
        # Set OpenCV video-capture parameters
        self.camera_num = camera
        self.camera = cv2.VideoCapture(self.camera_num)
        self.is_running = False
        self.__scale = scale
        
        # Configure PyTorch MiDaS
        modes = {
            "standard": False,
            "live": True
        } 
        self.live_render = modes.get(mode, None)
        if self.live_render is None:
            raise ValueError(f'Unrecognized mode given: \"{mode}\"')
        
        self.model_type = "MiDaS_small" if self.live_render else "DPT_Large"
        self.model = torch.hub.load("intel-isl/MiDaS", self.model_type)
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = midas_transforms.small_transform if self.live_render else midas_transforms.dpt_transform
        print(f'Starting up depth scanner, running {mode} mode')
        
    def __repr__(self) -> str:
        return f'<DepthScanner | camera={self.camera_num}, device={str(self.__device).upper()}>'
    
    @property
    def device(self) -> str:
        return str(self.__device)
    
    @staticmethod
    def __normalize(frame, bits:int) -> np.ndarray:
        """
        Normalize the given map for OpenCV.

        Args:
            frame (np.ndarray): Frame image
            bits (int): image bits

        Returns:
            np.ndarray: Normalized depth map
        """
        depth_min = frame.min()
        depth_max = frame.max()
        max_val = (2 ** (8 * bits)) - 1
        
        if depth_max - depth_min > np.finfo("float").eps:
            out = max_val * (frame - depth_min) / (depth_max - depth_min)
        else:
            out = np.zeros(frame.shape, dtype=frame.type)
            
        if bits == 1:
            return out.astype("uint8")
        return out.astype("uint16")
    
    @staticmethod
    def __resize(image, factor:float=1.0) -> np.ndarray:
        """_summary_

        Args:
            image (np.ndarray): Image to scale
            factor (float, optional): Scaling factor. Defaults to 1.0.

        Returns:
            np.ndarray: _description_
        """
        height, width, _ = image.shape
        new_dimensions = (round(width * factor), round(height * factor))
        return cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)
        
    
    def get_depth(self, frame) -> np.ndarray:
        """
        Apply MiDaS model to generate monocular depth estimation 
        of an image frame.

        Args:
            frame (np.ndarray): Image frame

        Returns:
            np.ndarray: Converted depth map
        """
        try:
            input_batch = self.transform(frame).to(self.__device)
            with torch.no_grad():
                prediction = self.model(input_batch)
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=frame.shape[:2],
                    mode="bicubic",
                    align_corners=False,
                ).squeeze()
            depth_frame = prediction.cpu().numpy()
            return self.__normalize(depth_frame, bits=2)
        
        except Exception as e:
            print(f'Failed to generate depth map: {e}')
            return None
    
    def colormap(self, image):
        depth_map = self.get_depth(image)
        depth_map = (depth_map/256).astype(np.uint8)
        return cv2.applyColorMap(depth_map, cv2.COLORMAP_HOT)
    
    def capture(self, frame) -> None:
        """
        Capture a camera frame and render a depth map.

        Args:
            frame (np.ndarray): Camera capture frame
        """
        colored_map = self.colormap(frame)  # Preprocess frame
        
        # Display colored depth map
        date_today = dt.datetime.now().strftime("%d %B %Y")
        timestamp = dt.datetime.now().strftime("%H:%M:%S")
        print(f'[{date_today} | {timestamp}] Frame captured!')
        cv2.imshow(f'Depth Scan - {timestamp}', colored_map)
    
    def run(self) -> None:
        """
        Run the video camera.
        """
        self.is_running = True
        print(f'[{self.device.upper()}] Running depth scan...')
        
        try:
            while self.is_running:
                frame_start_time = perf_counter()
                ret, frame = self.camera.read()
                display_frame = self.colormap(frame) if self.live_render else frame
                frame_end_time = perf_counter()
                fps = round(1 / (frame_end_time - frame_start_time))
                window_label = "Depth Capture" if self.live_render else "Standard Camera" 
                cv2.putText(display_frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (10, 255, 100), 2)
                cv2.imshow(window_label, self.__resize(display_frame, factor=self.__scale))

                key = cv2.waitKey(10)
                if key == 32 and not self.live_render:
                    self.capture(frame)  # Capture frame on spacebar press
                if key == 27:
                    print("Closing scanner...")  # Close windows when Esc is pressed
                    self.is_running = False
                    break
                
        except Exception as e:
            print(f'Error during camera streaming: {e}')
            
        finally:
            self.camera.release()
            cv2.destroyAllWindows()
            
        print("Scanner closed!")
        