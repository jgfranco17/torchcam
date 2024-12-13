from dataclasses import dataclass
from typing import Dict, Final

import cv2

from .errors import TorchcamInputError


@dataclass(frozen=True)
class KeyboardKeys:
    ESC: Final[int] = 27
    SPACE: Final[int] = 32
    LETTER_Q: Final[int] = ord("q")
    LETTER_C: Final[int] = ord("c")


class DepthMapColors:
    COLOR_SCHEMES: Dict[str, int] = {
        "autumn": cv2.COLORMAP_AUTUMN,
        "rainbow": cv2.COLORMAP_RAINBOW,
        "bone": cv2.COLORMAP_BONE,
        "jet": cv2.COLORMAP_JET,
        "ocean": cv2.COLORMAP_OCEAN,
        "deepgreen": cv2.COLORMAP_DEEPGREEN,
        "hot": cv2.COLORMAP_HOT,
        "inferno": cv2.COLORMAP_INFERNO,
    }
    DEFAULT: Final[int] = cv2.COLORMAP_INFERNO

    @classmethod
    def get_color(cls, key: str) -> int:
        return cls.COLOR_SCHEMES.get(key, cls.DEFAULT)


@dataclass(frozen=True)
class MidasTorch:
    # MiDaS source
    MIDAS_SOURCE: Final[str] = "intel-isl/MiDaS"
    # Model sizes
    MODEL_SMALL: Final[str] = "MiDaS_small"
    MODEL_MEDIUM: Final[str] = "DPT_Hybrid"
    MODEL_LARGE: Final[str] = "DPT_Large"
    # Device type
    DEVICE_CPU: Final[str] = "cpu"
    DEVICE_GPU: Final[str] = "cuda"
