"""
Entry point for CLI tool.
"""
import sys
import argparse
import importlib


def main():
    parser = argparse.ArgumentParser("Say hello to the world")
    parser.add_argument("command", type=str, help="Which command to run")

    args = parser.parse_args()
    try:
        module = importlib.import_module(f'src.commands.{args.command}')

    except ModuleNotFoundError:
        print(f'Invalid command: {args.command}')
        sys.exit(1)

    getattr(module, "Command")().run()
