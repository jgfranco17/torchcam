"""
CLI base for TorchCam project.
"""
import io
import os
import argparse
from torchcam.camera import DepthCamera


def read(*paths, **kwargs):
    """
    Read the contents of a text file safely.
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def config():
    parser = argparse.ArgumentParser("TORCHCAM")
    parser.add_argument("mode",
                        type=str,
                        help="Set to \'live\' for live depth-capture, or \'standard\' otherwise")
    parser.add_argument("--camera", "-c",
                        type=int,
                        default=0,
                        help="Webcam port to capture, default is 0")
    parser.add_argument("--window", "-w",
                        type=float,
                        default=1.0,
                        help="Display window scale, default is 1")
    parser.add_argument("--style", "-s",
                        type=str,
                        default="hot",
                        help="Colormap styling")
    args = parser.parse_args()
    return args


def main():
    """
    The main function executes on commands:
    `python -m depth-camera` and `$ depth-camera `.
    """
    args = config()
    scanner = DepthCamera(camera=args.camera, mode=args.mode, scale=args.window, color=args.style)
    scanner.run()
