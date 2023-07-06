import argparse
from torchcam.camera import DepthCamera
from torchcam.cli import get_configs


if __name__ == "__main__":
    args = get_configs()
    scanner = DepthCamera(camera=args.camera, mode=args.mode, scale=args.window, color=args.style)
    scanner.run()
    