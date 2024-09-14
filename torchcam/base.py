from typing import Optional

import cv2
import numpy as np
import torch


class DepthEstimator:
    def __init__(
        self, mode: Optional[str] = "standard", color: Optional[str] = "hot"
    ) -> None:
        """
        Depth estimator module architecture. Sets the color
        mapping and runs main calculations using MiDaS model.

        Args:
            mode (str, optional): Set camera to 'live' or 'standard'
            color (str, optional): Colormap display style

        Raises:
            ValueError: If invalid colormap scheme is provided
            ValueError: If invalid scan mode is given
        """
        # Set colormap styling
        map_style = {
            "autumn": cv2.COLORMAP_AUTUMN,
            "rainbow": cv2.COLORMAP_RAINBOW,
            "bone": cv2.COLORMAP_BONE,
            "jet": cv2.COLORMAP_JET,
            "ocean": cv2.COLORMAP_OCEAN,
            "deepgreen": cv2.COLORMAP_DEEPGREEN,
            "hot": cv2.COLORMAP_HOT,
            "inferno": cv2.COLORMAP_INFERNO,
        }
        if color.lower() not in map_style.keys():
            raise ValueError(f'Invalid colormap color "{color}" provided.')
        self.map_color = map_style.get(color.lower())

        # Configure PyTorch MiDaS
        modes = {"standard": False, "live": True}
        self.live_render = modes.get(mode, None)
        if self.live_render is None:
            raise ValueError(f'Unrecognized mode given: "{mode}"')

        self.model_type = "MiDaS_small" if self.live_render else "DPT_Large"
        self.model = torch.hub.load("intel-isl/MiDaS", self.model_type)
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.__device)
        self.model.eval()
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = (
            midas_transforms.small_transform
            if self.live_render
            else midas_transforms.dpt_transform
        )

    @property
    def device(self) -> str:
        """
        Returns the device used to run MiDaS model
        """
        return str(self.__device).upper()

    @staticmethod
    def __normalize(frame: np.ndarray, bits: int) -> np.ndarray:
        """
        Normalize the given map for OpenCV.

        Args:
            frame (np.ndarray): Frame image
            bits (int): image bits

        Returns:
            np.ndarray: Normalized depth map
        """
        if bits <= 0:
            raise ValueError(f"Bitsize must be positive integer.")

        depth_min = frame.min()
        depth_max = frame.max()
        max_val = (2 ** (8 * bits)) - 1

        if depth_max - depth_min > np.finfo("float").eps:
            out = max_val * (frame - depth_min) / (depth_max - depth_min)
        else:
            out = np.zeros(frame.shape, dtype=frame.dtype)

        if bits == 1:
            return out.astype("uint8")
        return out.astype("uint16")

    def get_depth(self, frame: np.ndarray) -> np.ndarray:
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
            print(f"Failed to generate depth map: {e}")
            return np.zeros(frame.shape)

    def colormap(self, image: np.ndarray) -> np.ndarray:
        """
        Recolor the depth map from grayscale to colored

        Args:
            image (np.ndarray): Grayscale image

        Returns:
            np.ndarray: Colored map image
        """
        depth_map = self.get_depth(image)
        depth_map = (depth_map / 256).astype(np.uint8)
        return cv2.applyColorMap(depth_map, self.map_color)
