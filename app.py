from depthscan import DepthScanner


if __name__ == "__main__":
    scanner = DepthScanner(camera=0)
    scanner.run()
    