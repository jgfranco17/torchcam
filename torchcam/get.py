"""
CLI base for TorchCam project.
"""
import logging

import click

from .camera.resources import list_ports

logger = logging.getLogger(__name__)


@click.group("get")
def get_group() -> None:
    """Check estimator resources."""
    pass


@click.command("inputs")
def get_available_camera_inputs() -> None:
    """See which camera input ports are available for use"""
    _, working_ports = list_ports()
    print(f"The following ports are working: {working_ports}")


get_group.add_command(get_available_camera_inputs)
