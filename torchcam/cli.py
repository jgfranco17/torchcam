"""
CLI base for TorchCam project.
"""
import io
import os
import argparse
from torchcam.camera import DepthCamera


def read(*paths, **kwargs) -> str:
    """
    Read the contents of a text file safely.
    
    Returns:
        str: The contents of the file
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def config() -> argparse.Namespace:
    """
    Creates a parsed configuration namespace from the CLI arguments.

    Returns:
        argparse.Namespace: Configuration namespace
    """
    parser = argparse.ArgumentParser(
        prog="torchcam",
        description="Applying PyTorch MiDaS model on live webcam capture."
    )
    parser.add_argument(
        "mode",
        type=str,
        help="Set to \'live\' for live depth-capture, or \'standard\' for single image capture."
    )
    parser.add_argument(
        "--camera", "-c",
        type=int,
        default=0,
        help="Webcam port to capture, default is 0"
    )
    parser.add_argument(
        "--window", "-w",
        type=float,
        default=1.0,
        help="Display window scale, default is 1"
    )
    parser.add_argument(
        "--style", "-s",
        type=str,
        default="hot",
        help="Colormap styling, default is \'hot\'"
    )
    args = parser.parse_args()
    return args


def main():
    """
    The main function executes on commands:
    `python -m torchcam` and `$ torchcam`.
    """
    args = config()
    scanner = DepthCamera(camera=args.camera, mode=args.mode, scale=args.window, color=args.style)
    scanner.run()
