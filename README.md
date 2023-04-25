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
* [Authors](#authors)

## 🔎 About <a name = "about"></a>

This project uses PyTorch's [MiDaS](https://pytorch.org/hub/intelisl_midas_v2/) model to generate live depth estimation streams using a webcam. By applying the MiDaS model to the video stream from the webcam, the software is able to generate a real-time colored depth map of the scene being captured. Runs better if [GPU is available](https://pytorch.org/docs/stable/notes/cuda.html), as the video stream can render depth maps faster.

## 🔧 Project Structure <a name = "structure"></a>

```text
jgfranco17/depth-camera/
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
│   └── test_main.py                    Primary unittests
├── .gitignore                          List of files to be ignored for Git 
├── LICENSE                             Project license
├── Makefile                            Build scripts for setup and usage
├── pyproject.toml                      Definition of package build process using TOML
├── README.md                           Project overview and outline
├── requirements.txt                    Python library dependencies
├── requirements-test.txt               Testing and linting dependencies for development
├── setup.cfg                           Setup configuration of the Python package
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

To get started with this project, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/depth-camera.git
cd depth-camera
pip install -r requirements.txt
```

## 🚀 Usage <a name = "usage"></a>

### CLI usage

To run the depth estimation stream, simply execute the following command:

```bash
python3 app.py --camera CAMERA_NUMBER --mode [live|standard]
```

### Config options

camera: webcam number, `0` refers to the default webcam of the computer  

mode:  
- `standard` - Displays plain camera view, press `c` key to capture and convert to depth map
- `live` - Displays live depth map render, lower frame rate due to conversion per frame

## ⛏️ Built Using <a name = "built_using"></a>
![OpenCV](https://img.shields.io/badge/PyTorch-1.13.0-orange?style=for-the-badge&logo=pytorch&logoColor=orange) ![OpenCV](https://img.shields.io/badge/OpenCV-4.6.0-orange?style=for-the-badge&logo=opencv&logoColor=orange) ![NumPy](https://img.shields.io/badge/numpy-1.23.4-orange?style=for-the-badge&logo=numpy&logoColor=orange)

## ✍️ Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)
