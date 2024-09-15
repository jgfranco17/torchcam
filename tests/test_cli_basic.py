from tests.conftest import TestRunner


def test_help_message_sane(runner: TestRunner) -> None:
    """Test a sane basic help call."""
    result = runner.run_cli(["--help"])
    assert result.exit_code == 0
    assert "Torchcam: a monocular depth estimation tool using PyTorch" in result.output
