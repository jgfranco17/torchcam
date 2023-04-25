"""CLI interface for project_template project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import argparse
from .camera import DepthScanner


def _config():    
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m",
                        type=str,  
                        default="standard", 
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


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m project_template` and `$ project_template `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    args = _config()
    scanner = DepthScanner(camera=args.camera, mode="live", scale=args.scale, color=args.color)
    scanner.run()
