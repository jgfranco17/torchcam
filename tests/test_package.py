import pytest

from torchcam.base import DepthEstimator
from torchcam.camera import DepthCamera


def test_depth_estimator_invalid_color_map():
    """
    Test that an error is raised when an invalid colormap is provided.
    """
    with pytest.raises(ValueError):
        invalid_estimator = DepthEstimator(color="invalid_color")


def test_depth_estimator_invalid_scan_mode():
    """
    Test that an error is raised when an invalid scan mode is provided.
    """
    with pytest.raises(ValueError):
        DepthEstimator(mode="invalid_mode")
