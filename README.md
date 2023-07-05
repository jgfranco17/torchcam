<h1 align="center">Monocular Depth Camera</h1>

<div align="center">

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## 📝 Table of Contents

* [About](#about)
* [Project Structure](#structure)
* [Getting Started](#getting_started)
* [Usage](#usage)
* [Testing](#testing)
* [Authors](#authors)

## 🔎 About <a name = "about"></a>

This project uses PyTorch's [MiDaS](https://pytorch.org/hub/intelisl_midas_v2/) model to generate live depth estimation streams using a webcam. By applying the MiDaS model to the video stream from the webcam, the software is able to generate a real-time colored depth map of the scene being captured. Runs better if [GPU is available](https://pytorch.org/docs/stable/notes/cuda.html), as the video stream can render depth maps faster.

## 🔧 Project Structure <a name = "structure"></a>

```text
jgfranco17/torchcam/
├── .github/                            Github Actions suite
│   │   ├── workflows                   GA workflows
│   │   │   └── python-test.yml         Test installation on different Python versions
│   │   └── ISSUE_TEMPLATES             Templates for requests/reports
│   │       ├── bug_report.md           Reporting a bug          
│   │       └── feature_request.md      Request implementation of a new feature
├── depthscan/                          Python package directory
│   ├── __init__.py                     Makes the directory a package
│   ├── __main__.py                     Entrypoint for CLI tools
│   ├── base.py                         Architecture for estimator
│   ├── camera.py                       Camera model module
│   ├── cli.py                          Adds CLI implementation
│   └── VERSION                         Project version
├── tests/                              PyTest suite
│   ├── __init__.py                     Makes the directory a test module
│   ├── conftest.py                     Fixtures for reusability in testing
│   ├── test_cv.py                      Unittests for OpenCV
│   ├── test_package.py                 Unittests for the package scripts
│   └── test_torch.py                   Unittests for PyTorch
├── app.py                              Base runnable script
├── .gitignore                          List of files to be ignored for Git 
├── LICENSE                             Project license
├── Makefile                            Build scripts for setup and usage
├── pyproject.toml                      Definition of package build process using TOML
├── README.md                           Project overview and outline
├── requirements.txt                    Python library dependencies
├── requirements-test.txt               Testing and linting dependencies for development
└── setup.py                            Build project with setuptools
```

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to use this project, you will need to have the following software and libraries installed:  
* PyTorch
* OpenCV
* NumPy

### Installing

To get started with this project for development purposes, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/torchcam.git
cd torchcam
pip install -r requirements.txt
```

## 🔧 Testing <a name = "testing"></a>

In order to run diagnostics and unittests, install the testing dependencies found in the `requirements-test.txt` file. This will allow you to utilize the full capacity of the test modules we have built.

To run the full test suite, run the Makefile command as follows:

```bash
make test
```

This will run the test module and generates a detailed result report.

### Using PyTest CLI

You can run these tests using the [PyTest](https://docs.pytest.org/en/7.3.x/) CLI. To run all tests in the directory containing the test files, navigate to the directory and enter `pytest` in the command line; for added verbosity, add the `-vv` flag after. To run a specific test file, enter `pytest <filename>`.

```bash
# Run all tests in the testing module with full detail
cd torchcam
pytest -vv

# Run a specific test file
cd torchcam/tests
pytest test_package.py
```

### Why these tests are important

Running these unittests is necessary to ensure that the code is functioning as expected and meeting the requirements of the design specification. The unittests are designed to test each function and method of the code and to identify any errors or unexpected behavior. By testing the code using these PyTest unittests, we can ensure that the code meets the specified requirements and that any changes made to the code do not introduce new bugs or errors.

In addition, these tests can be automated to run on every code change, allowing us to quickly identify any issues that may arise and enabling us to maintain a high level of code quality. 

In essence, running these PyTest unittests is a critical part of the software QA process and helps to ensure that our code is robust, reliable, and meets the needs of our end-users before the product hits deployment.

## 🚀 Usage <a name = "usage"></a>

### CLI usage

To run the depth estimation stream, simply execute the following command:

```bash
# Use the prebuilt Makefile
make run

# Specify your own configuration
python3 app.py --camera <camera number> --mode [live|standard]
```

### Config options

camera: webcam number, `0` refers to the default webcam of the computer  

mode:  
- `standard` - Displays plain camera view, press `c` key to capture and convert to depth map
- `live` - Displays live depth map render, lower frame rate due to conversion per frame

### Running as CLI tool

To run as an installed CLI tool, use the pip manager to install via setuptools.

```bash
cd torchcam
pip install .
```

From there, the tool can be used similarly to above, only this time the `python3 app.py` can be replaced with `torchcam`.

A PyPi implementation is in the works, and instructions to install via official channels will be posted here when available.

## ⛏️ Built Using <a name = "built_using"></a>
![OpenCV](https://img.shields.io/badge/PyTorch-1.13.0-orange?style=for-the-badge&logo=pytorch&logoColor=orange) ![OpenCV](https://img.shields.io/badge/OpenCV-4.6.0-orange?style=for-the-badge&logo=opencv&logoColor=orange) ![NumPy](https://img.shields.io/badge/numpy-1.23.4-orange?style=for-the-badge&logo=numpy&logoColor=orange)

## ✍️ Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)
