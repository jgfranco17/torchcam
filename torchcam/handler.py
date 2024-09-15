import logging
import sys
from typing import Any, Dict

import click

from .camera.errors import ExitCode, TorchcamBaseError
from .output import print_warning

logger = logging.getLogger(__name__)


class TorchcamCliHandler(click.Group):
    """A wrapped around CLI invocation that handles related errors."""

    AUTHOR_DETAILS: Dict[str, str] = {
        "Author": "Chino Franco",
        "Github": "https://github.com/jgfranco17",
    }

    def invoke(self, ctx: click.Context) -> Any:
        """Invoke the CLI and catch, log and exit for any raised errors."""
        try:
            return super().invoke(ctx)

        except TorchcamBaseError as err:
            logger.exception(err)
            print_warning(f"{err.help_text}")
            sys.exit(err.exit_code)

        except click.UsageError as err:
            err.show()
            sys.exit(ExitCode.RUNTIME_ERROR)

    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        """Customize help info."""
        super().format_help(ctx, formatter)
        details = "\n".join(
            [f"{key}: {value}" for key, value in self.AUTHOR_DETAILS.items()]
        )
        formatter.write(f"\n{details}")
