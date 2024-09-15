"""
CLI base for TorchCam project.
"""
import logging

import click

from .camera.depth_camera import DepthCamera

logger = logging.getLogger(__name__)


@click.group("run")
def run_group() -> None:
    """Run the camera"""
    pass


@click.command("live")
@click.option(
    "--camera",
    "-c",
    type=int,
    help="Webcam port to capture",
    default=0,
)
@click.option(
    "--window",
    "-w",
    type=float,
    help="Display window scale, default is 1",
    default=1.0,
)
@click.option(
    "--style",
    "-s",
    type=str,
    help="Colormap styling, default is 'hot'",
    default="hot",
)
def run_live_view(camera: int, window: float, style: str) -> None:
    """Run live estimation on webcam input."""
    scanner = DepthCamera(camera=camera, mode="live", scale=window, color=style)
    scanner.run()


@click.command("standard")
@click.option(
    "--camera",
    "-c",
    type=int,
    help="Webcam port to capture",
    default=0,
)
@click.option(
    "--window",
    "-w",
    type=float,
    help="Display window scale, default is 1",
    default=1.0,
)
def run_standard_view(camera: int, window: float) -> None:
    """Run standard webcam, capture input on command."""
    scanner = DepthCamera(camera=camera, mode="standard", scale=window, color="hot")
    scanner.run()


run_group.add_command(run_live_view)
run_group.add_command(run_standard_view)
