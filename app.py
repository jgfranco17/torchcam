from depthscan import config, DepthScanner


if __name__ == "__main__":
    args = config()
    scanner = DepthScanner(camera=args.camera, mode=args.mode, scale = args.window)
    scanner.run()
    