from dataclasses import dataclass
from typing import Dict, Final

import cv2

from .errors import TorchcamInputError


@dataclass(frozen=True)
class KeyboardKeys:
    ESC: Final[int] = 20
    SPACE: Final[int] = 32
    LETTER_Q: Final[int] = ord("q")


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
