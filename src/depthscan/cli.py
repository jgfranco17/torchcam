from typer import Typer

app = Typer()

@app.command()
def hello():
    print("Hello.")

@app.command()
def bye(name: str):
    print(f"Bye {name}")