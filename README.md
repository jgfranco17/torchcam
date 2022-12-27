# Monocular Depth Camera

This project uses PyTorch's MiDaS model to generate live depth estimation streams using a webcam. By applying the MiDaS model to the video stream from the webcam, the software is able to generate a real-time colored depth map of the scene being captured. Runs better if GPU is available, as the video stream can render depth maps faster.

## Requirements
In order to use this project, you will need to have the following software and libraries installed:  
- PyTorch
- OpenCV
- NumPy

## Setup

To get started with this project, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/depth-camera.git
cd depth-camera
pip install -r requirements.txt
```

## Usage

### Run commands

To run the depth estimation stream, simply execute the following command:

```bash
python3 app.py --camera CAMERA_NUMBER --mode [live|standard]
```

### Config options

camera: webcam number, `0` refers to the default webcam of the computer  

mode:  
- standard -> Displays plain camera view, press `c` key to capture and convert to depth map
- live -> Displays live depth map render, lower frame rate due to conversion per frame