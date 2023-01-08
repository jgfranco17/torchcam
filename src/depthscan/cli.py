from typer import Typer
from depthscan import DepthScanner

app = Typer()

@app.command()
def live(camera:int=0, scale:float=1.0, color:str="hot"):
    scanner = DepthScanner(camera=camera, mode="live", scale=scale, color=color)
    scanner.run()