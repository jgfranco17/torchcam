import cv2
import pytest

from .conftest import webcam


def test_video_capture(webcam):
    """
    Test webcam video capture using OpenCV
    """
    assert webcam.isOpened(), "Webcam failed to open"
    ret, frame = webcam.read()
    assert ret, "Failed to read frame from webcam"


def test_video_capture_frame_rate(webcam):
    """
    Test that the video capture cycles through the feed.
    """
    fps = webcam.get(cv2.CAP_PROP_FPS)
    assert fps > 0, "Invalid frame rate"


def test_video_capture_resolution(webcam):
    """
    Test that a valid frame is formed.
    """
    width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    assert width > 0 and height > 0, "Invalid resolution"
