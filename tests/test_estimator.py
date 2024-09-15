import pytest

from torchcam.camera.base import DepthEstimator
from torchcam.camera.errors import TorchcamInputError


def test_depth_estimator_invalid_color_map():
    """
    Test that an error is raised when an invalid colormap is provided.
    """
    with pytest.raises(TorchcamInputError):
        _ = DepthEstimator(color="invalid_color")


def test_depth_estimator_invalid_scan_mode():
    """
    Test that an error is raised when an invalid scan mode is provided.
    """
    with pytest.raises(TorchcamInputError):
        _ = DepthEstimator(mode="invalid_mode")
