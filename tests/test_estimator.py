import pytest

from torchcam.camera.constants import DepthMapColors, MidasTorch
from torchcam.camera.errors import TorchcamInputError
from torchcam.camera.estimator import DepthEstimator

from .conftest import MockPytorchModel


def test_depth_estimator_init_default(mock_torch_model: MockPytorchModel):
    mode = "standard"
    color = "hot"
    depth_estimator = DepthEstimator(mode, color)

    assert depth_estimator.live_render is False
    assert depth_estimator.map_color == DepthMapColors.COLOR_SCHEMES.get("hot")
    assert depth_estimator.model_type == MidasTorch.MODEL_LARGE
    assert depth_estimator.label == "Standard Camera"
    assert depth_estimator.model is not None


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
