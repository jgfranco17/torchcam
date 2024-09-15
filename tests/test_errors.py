from torchcam.camera.errors import (
    ExitCode,
    TorchcamBaseError,
    TorchcamInputError,
    TorchcamRuntimeError,
)


def test_custom_base_error():
    message = "Base error occurred"
    exit_code = ExitCode.RUNTIME_ERROR
    help_text = "This is a help text"
    error = TorchcamBaseError(message, exit_code, help_text)
    assert error.message == message
    assert error.exit_code == exit_code
    assert error.help_text == help_text


def test_custom_sub_error_default_help_text():
    message = "Runtime error occurred"
    errors = [
        (TorchcamRuntimeError(message), ExitCode.RUNTIME_ERROR),
        (TorchcamInputError(message), ExitCode.INPUT_ERROR),
    ]
    for error, expected_exit_code in errors:
        assert error.message == message
        assert error.exit_code == expected_exit_code
        assert error.help_text is not None
        assert "Help is available" in error.help_text


def test_custom_sub_error_custom_help_text():
    error_message = "Some error occurred"
    help_text = "Custom help text"
    errors = [
        (TorchcamRuntimeError(error_message, help_text), ExitCode.RUNTIME_ERROR),
        (TorchcamInputError(error_message, help_text), ExitCode.INPUT_ERROR),
    ]
    for error, expected_exit_code in errors:
        assert error.message == error_message
        assert error.exit_code == expected_exit_code
        assert error.help_text is not None
        assert help_text in error.help_text
