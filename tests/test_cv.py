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
    # Get the frame rate of the webcam
    fps = webcam.get(cv2.CAP_PROP_FPS)

    # Check that the frame rate is a positive number
    assert fps > 0, "Invalid frame rate"


def test_video_capture_resolution(webcam):
    """
    Test that a valid frame is formed.
    """
    # Get the resolution of the webcam
    width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Check that the resolution is a positive number
    assert width > 0 and height > 0, "Invalid resolution"