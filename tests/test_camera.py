from unittest.mock import MagicMock

from pytest import LogCaptureFixture, MonkeyPatch

from torchcam.camera.depth_camera import DepthCamera

from .conftest import MockPytorchModel


def test_camera_init_default(
    mock_torch_model: MockPytorchModel,
    mock_torch_device_cuda: MagicMock,
    monkeypatch: MonkeyPatch,
    caplog: LogCaptureFixture,
):
    webcam_runner = DepthCamera()
    mock_torch_device_cuda.is_available.return_value = False

    assert webcam_runner.camera_num == 0
    assert webcam_runner.is_running is False
