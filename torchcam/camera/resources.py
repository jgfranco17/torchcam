import logging
from typing import List, Tuple

import cv2

logger = logging.getLogger(__name__)


def list_ports() -> Tuple[List[int], List[int]]:
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    working_ports = []
    available_ports = []

    for port in range(10):
        try:
            camera = cv2.VideoCapture(port)
            if camera.isOpened():
                is_reading, _ = camera.read()
                if is_reading:
                    working_ports.append(port)
                else:
                    available_ports.append(port)
        except:
            logger.debug(f"Attempted to open port {port} but failed, skipping...")

    return available_ports, working_ports
