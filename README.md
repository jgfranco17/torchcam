<h1 align="center">Monocular Depth Camera</h1>

<div align="center">

![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/github/license/jgfranco17/depth-camera?color=blue)

</div>

## 📝 Table of Contents

* [About](#about)
* [Project Structure](#structure)
* [Getting Started](#getting_started)
* [Usage](#usage)
* [Authors](#authors)

## 🔎 About <a name = "about"></a>

This project uses PyTorch's [MiDaS](https://pytorch.org/hub/intelisl_midas_v2/) model to generate live depth estimation streams using a webcam. By applying the MiDaS model to the video stream from the webcam, the software is able to generate a real-time colored depth map of the scene being captured. Runs better if [GPU is available](https://pytorch.org/docs/stable/notes/cuda.html), as the video stream can render depth maps faster.

## 🔧 Project Structure <a name = "structure"></a>

```
/depth-camera/
├── src/                            Source dir.
│   └── depthscan/                  Python package directory.
│       ├── __init__.py             Makes the directory a package.
│       ├── cli.py                  Adds CLI implementation.
│       └── camera.py               Camera model module.
├── pyproject.toml                  Definition of package build process.
├── README.md                       Project overview and outline.
└── setup.cfg                       Setup configuration of the Python package.
```

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

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
![OpenCV](https://img.shields.io/badge/PyTorch-1.13.0-green?style=for-the-badge&logo=pytorch) ![OpenCV](https://img.shields.io/badge/OpenCV-4.6.0-green?style=for-the-badge&logo=opencv) ![NumPy](https://img.shields.io/badge/numpy-1.23.4-green?style=for-the-badge&logo=numpy)

## ✍️ Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)
