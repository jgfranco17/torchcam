import cv2
import torch
import pytest


def test_video_capture(webcam):
    """
    Test webcam video capture using OpenCV
    """
    assert webcam.isOpened(), "Webcam failed to open"
    ret, frame = webcam.read()
    assert ret, "Failed to read frame from webcam"


def test_torch_tensor_creation(basic_tensor):
    """
    Verify the creation of PyTorch tensors.
    """
    assert basic_tensor.shape == (3, 224, 224), "Incorrect tensor shape"
    assert basic_tensor.dtype == torch.float32, "Incorrect tensor type"
    assert torch.min(basic_tensor) >= -1.0, "Tensor values outside of range"
    assert torch.max(basic_tensor) <= 1.0, "Tensor values outside of range"


def test_tensor_multiplication():
    """
    Verify the operations of PyTorch tensors
    """
    tensor1 = torch.randn((3, 224, 224))
    tensor2 = torch.randn((3, 224, 224))

    # Multiply tensors element-wise
    tensor_product = tensor1 * tensor2

    # Check tensor shape and type
    assert tensor_product.shape == (3, 224, 224), "Incorrect tensor shape"
    assert tensor_product.dtype == torch.float32, "Incorrect tensor type"


def test_tensor_construction():
    """
    Check the generation of new tensors from Python built-ins
    """
    tensor = torch.tensor([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Check tensor shape and type
    assert tensor.shape == (3, 3), "Incorrect tensor shape"
    assert tensor.dtype == torch.int64, "Incorrect tensor type"


def test_video_capture_frame_rate(webcam):
    # Get the frame rate of the webcam
    fps = webcam.get(cv2.CAP_PROP_FPS)

    # Check that the frame rate is a positive number
    assert fps > 0, "Invalid frame rate"


def test_video_capture_resolution(webcam):
    # Get the resolution of the webcam
    width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Check that the resolution is a positive number
    assert width > 0 and height > 0, "Invalid resolution"
