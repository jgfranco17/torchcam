import logging

import click
from colorama import Fore, Style


class ColorHandler(logging.StreamHandler):
    def emit(self, record: logging.LogRecord) -> None:
        colors = {
            logging.DEBUG: Fore.CYAN,
            logging.INFO: Fore.GREEN,
            logging.WARNING: Fore.YELLOW,
            logging.ERROR: Fore.RED,
            logging.CRITICAL: Fore.RED,
        }
        color = colors.get(record.levelno, Fore.WHITE)
        record.msg = f"{color}{record.msg}{Style.RESET_ALL}"
        super().emit(record)


def print_error(message: str) -> None:
    """
    Print an error message in red.

    Args:
        message (str): The error message to print.
    """
    click.echo(f"{Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """
    Print a warning message in yellow.

    Args:
        message (str): The warning message to print.
    """
    click.echo(f"{Fore.YELLOW}{Style.BRIGHT}{message}{Style.RESET_ALL}")


def print_success(message: str) -> None:
    """
    Print a success message in green.

    Args:
        message (str): The success message to print.
    """
    click.echo(f"{Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}")
