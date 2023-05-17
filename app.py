import argparse
from torchcam.camera import DepthCamera
from torchcam.cli import config


if __name__ == "__main__":
    args = config()
    scanner = DepthCamera(camera=args.camera, mode=args.mode, scale=args.window, color=args.style)
    scanner.run()
    