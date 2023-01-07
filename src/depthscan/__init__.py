import argparse
from .camera import DepthScanner

def config():    
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
    