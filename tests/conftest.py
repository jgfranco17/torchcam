import logging
from copy import deepcopy
from typing import Generator, List, Tuple
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner, Result

from torchcam.main import cli
from torchcam.output import ColorHandler


class TestRunner:
    def __init__(self):
        self.env = {
            "GITHUB_USERNAME": "test-user",
            "GITHUB_API_TOKEN": "my-github-api-token",  # pragma: allowlist secret
        }
        self.__runner = CliRunner(mix_stderr=False)

    @property
    def directory(self) -> str:
        return self.__working_dir

    def run_cli(self, cli_args: List[str]) -> Result:
        """Run the Torchcam CLI with envs set."""
        env = deepcopy(self.env)
        return self.__runner.invoke(cli, cli_args, env=env)


class MockLogger:
    def __init__(self) -> None:
        self.logger = logging.getLogger("mock-logger")
        self.logger.setLevel(logging.DEBUG)
        self.handler = ColorHandler()
        self.logger.addHandler(self.handler)

    def get_log_and_handler(self) -> Tuple[logging.Logger, ColorHandler]:
        return self.logger, self.handler


class MockPytorchModel(MagicMock):
    def __init__(self) -> None:
        pass

    def to(self, device: str):
        assert device in ("cpu", "cuda")

    def eval(self) -> None:
        pass


@pytest.fixture
def runner() -> TestRunner:
    return TestRunner()


@pytest.fixture
def logger() -> MockLogger:
    return MockLogger()


@pytest.fixture
def mock_torch_model() -> Generator[MockPytorchModel, None, None]:
    with patch("torchcam.camera.estimator.torch.hub.load"):
        mock_model = MockPytorchModel()
        yield mock_model


@pytest.fixture
def mock_torch_device_cuda() -> Generator[MagicMock, None, None]:
    with patch("torchcam.camera.estimator.torch.cuda") as mock_cuda:
        yield mock_cuda
