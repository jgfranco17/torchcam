from io import StringIO
from unittest.mock import patch

from colorama import Fore, Style

from tests.conftest import MockLogger


def test_color_handler_debug(logger: MockLogger):
    log, handler = logger.get_log_and_handler()
    log_stream = StringIO()
    handler.stream = log_stream

    log.debug("This is a debug message")
    log_output = log_stream.getvalue()
    assert Fore.CYAN in log_output
    assert Style.RESET_ALL in log_output
    assert "This is a debug message" in log_output


def test_color_handler_error(logger: MockLogger):
    log, handler = logger.get_log_and_handler()
    log_stream = StringIO()
    log_stream = StringIO()
    handler.stream = log_stream

    log.error("This is an error message")
    log_output = log_stream.getvalue()
    assert Fore.RED in log_output
    assert Style.RESET_ALL in log_output
    assert "This is an error message" in log_output
