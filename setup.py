"""
Python setup.py for depth-camera package
"""
import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """
    Read the contents of a text file safely.
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    """
    Read the requirements file line by line.
    """
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


# Run setup
setup(
    name="torchcam",
    version=read("torchcam", "VERSION"),
    description="Apply PyTorch MiDaS depth estimation on webcam feed.",
    url="https://github.com/jgfranco17/torchcam",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jgfranco17",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["torchcam = torchcam.__main__:main"]},
    extras_require={"test": read_requirements("requirements-test.txt")},
)
