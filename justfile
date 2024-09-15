# torchcam - Justfile utility

# Print list of available recipe (this)
default:
    @just --list --unsorted

# Run poetry install in all submodules
install:
    poetry install

# Run the CLI tool with Poetry
torchcam *ARGS:
    @poetry run torchcam {{ ARGS }}

# Build Docker image
build-docker:
    docker build -t torchcam .

# Run pytest via poetry
pytest *ARGS:
    poetry run pytest {{ ARGS }}

# Run test coverage
coverage:
    poetry run coverage run --source=torchcam --omit="*/__*.py,*/test_*.py" -m pytest
    poetry run coverage report -m
