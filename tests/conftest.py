import cv2
import pytest
import torch

from torchcam.base import DepthEstimator
from torchcam.camera import DepthCamera


@pytest.fixture(scope="module")
def webcam():
    cap = cv2.VideoCapture(0)
    yield cap
    cap.release()


@pytest.fixture(scope="module")
def basic_tensor():
    # Create a PyTorch tensor with random values
    tensor = torch.randn((3, 224, 224))
    yield tensor


@pytest.fixture(scope="module")
def depth_estimator():
    sample_estimator = DepthEstimator()
    yield sample_estimator


@pytest.fixture(scope="module")
def depth_camera():
    dc = DepthCamera()
    yield dc
