from typing import Any, Optional, Tuple

import cv2
import numpy as np
import torch

from .constants import DepthMapColors, MidasTorch
from .errors import TorchcamInputError


class DepthEstimator:
    """Depth estimator main class.

    Uses PyTorch's Midas model for generating estimated depth maps.
    """

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
            TorchcamInputError: If invalid colormap scheme is provided
            TorchcamInputError: If invalid scan mode is given
        """
        # Set colormap styling
        self.map_color = self.__get_colormap(color)

        # Configure PyTorch MiDaS
        modes = {"standard": False, "live": True}
        self.live_render = modes.get(mode, None)
        if self.live_render is None:
            raise TorchcamInputError(f'Unrecognized mode given: "{mode}"')

        self.model_type, self.label, self.transform = self.__configure_midas(
            self.live_render
        )
        self.model = torch.hub.load(MidasTorch.MIDAS_SOURCE, self.model_type)
        self.__device = self.__set_device()
        self.model.to(self.__device)
        self.model.eval()

    @staticmethod
    def __configure_midas(is_live: bool) -> Tuple[str, str, Any]:
        midas_transforms = torch.hub.load(MidasTorch.MIDAS_SOURCE, "transforms")
        return (
            (MidasTorch.MODEL_SMALL, "Depth Capture", midas_transforms.small_transform)
            if is_live
            else (
                MidasTorch.MODEL_LARGE,
                "Standard Camera",
                midas_transforms.dpt_transform,
            )
        )

    @property
    def device(self) -> str:
        """
        Returns the device used to run MiDaS model
        """
        return str(self.__device).upper()

    @staticmethod
    def __set_device() -> torch.device:
        device_type = (
            MidasTorch.DEVICE_GPU
            if torch.cuda.is_available()
            else MidasTorch.DEVICE_CPU
        )
        return torch.device(device_type)

    @staticmethod
    def __get_colormap(color: str) -> int:
        if color.lower() not in DepthMapColors.COLOR_SCHEMES.keys():
            raise TorchcamInputError(
                f"Invalid colormap color '{color}' provided",
                help_text=f"Must be one of the following: {DepthMapColors.COLOR_SCHEMES.keys()}",
            )
        return DepthMapColors.COLOR_SCHEMES.get(color, DepthMapColors.DEFAULT)

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
            raise TorchcamInputError(f"Bitsize must be positive integer.")

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
