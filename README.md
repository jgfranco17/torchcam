<h1 align="center">Torchcam: A Monocular Depth Camera</h1>

<div align="center">

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Testing](#testing)
- [Authors](#authors)

## 🔎 About <a name = "about"></a>

This project uses PyTorch's [MiDaS](https://pytorch.org/hub/intelisl_midas_v2/) model to generate live depth estimation streams
using a webcam. By applying the MiDaS model to the video stream from the webcam, the software is able to generate a real-time
colored depth map of the scene being captured. Runs better if [GPU is available](https://pytorch.org/docs/stable/notes/cuda.html),
as the video stream can render depth maps faster.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to use this project, you will need to have the following software and libraries installed:

- PyTorch
- OpenCV
- NumPy

### Installing

To get started with this project for development purposes, clone the repository to your local machine and install the required
dependencies.

```bash
git clone https://github.com/jgfranco17/torchcam.git
cd torchcam

pip install poetry pre-commit
pre-commit install
poetry install

# Use Poetry-based virtual environment
poetry shell
```

Pre-commit is required for commits to this repo. It is recommended to run it locally, as the CI also runs on pull request so
best to catch it early to save time.

## 🔧 Testing <a name = "testing"></a>

To run the full test suite, run the Makefile command as follows:

```bash
# Plain Pytest
poetry run pytest

# Run justfile script for testing
just coverage
```

This will run the test module and generates a detailed result report.

### Using PyTest CLI

You can run these tests using the [PyTest](https://docs.pytest.org/en/7.3.x/) CLI. To run all tests in the directory
containing the test files, navigate to the directory and enter `pytest` in the command line; for added verbosity, add
the `-vv` flag after. To run a specific test file, enter `pytest <filename>`.

```bash
# Run all tests in the testing module with full detail
cd torchcam
pytest -vv

# Run a specific test file
cd torchcam/tests
pytest test_package.py
```

### Why these tests are important

Running these unittests is necessary to ensure that the code is functioning as expected and meeting the requirements
of the design specification. The unittests are designed to test each function and method of the code and to identify
any errors or unexpected behavior. By testing the code using these PyTest unittests, we can ensure that the code
meets the specified requirements and that any changes made to the code do not introduce new bugs or errors.

In addition, these tests can be automated to run on every code change, allowing us to quickly identify any issues
that may arise and enabling us to maintain a high level of code quality.

In essence, running these PyTest unittests is a critical part of the software QA process and helps to ensure that
our code is robust, reliable, and meets the needs of our end-users before the product hits deployment.

## 🚀 Usage <a name = "usage"></a>

### CLI usage

To run the depth estimation stream, simply execute the following command:

```shell
# Use Poetry to run the CLI locally
$ poetry run torchcam

Usage: torchcam [OPTIONS] COMMAND [ARGS]...

  Torchcam: a monocular depth estimation tool using PyTorch.

Options:
  --version      Show the version and exit.
  -v, --verbose  Increase verbosity. Use multiple times for more detail (e.g. -vv for debug).
  --help         Show this message and exit.

Commands:
  run  Run the camera.

Author: Chino Franco
Github: https://github.com/jgfranco17
```

A PyPi implementation is in the works, and instructions to install via official channels will be posted here
when available.

## ⛏️ Built Using <a name = "built_using"></a>

![OpenCV](https://img.shields.io/badge/PyTorch-1.13.0-orange?style=for-the-badge&logo=pytorch&logoColor=orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.6.0-orange?style=for-the-badge&logo=opencv&logoColor=orange)
![NumPy](https://img.shields.io/badge/numpy-1.23.4-orange?style=for-the-badge&logo=numpy&logoColor=orange)

## ✍️ Authors <a name = "authors"></a>

### Primary

- [Chino Franco](https://github.com/jgfranco17)

### Contributors

- _Pending_
