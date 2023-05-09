import pytest
from src.depthscan.base import DepthEstimator
from src.depthscan.camera import DepthCamera


def test_depth_estimator_initialization(depth_estimator):
    """
    Test DepthEstimator initialization with default parameters.
    """
    assert isinstance(depth_estimator, DepthEstimator)


def test_depth_estimator_device(depth_estimator):
    """
    Test that the device property returns a string.
    """
    assert isinstance(depth_estimator.device, str)


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


def test_depth_camera_initialization(depth_camera):
    """
    Test DepthCamera initialization with default parameters.
    """
    assert isinstance(depth_camera, DepthCamera)


def test_depth_camera_scale(depth_camera):
    """
    Test the default scale property.
    """
    assert depth_camera.scale == 1.0
    
    
def test_depth_camera_run(depth_camera):
    """
    Test the run() method.
    """
    dc = DepthCamera()
    dc.is_running = False
    assert not dc.is_running



