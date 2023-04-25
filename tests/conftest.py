import cv2
import torch
import pytest


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
