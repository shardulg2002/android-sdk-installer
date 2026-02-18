from .tools import get_home_path
from .core import App

import click

@click.command()
@click.option("--path", default=str(get_home_path()), help="Specify the SDK installation path", type=click.Path(resolve_path=True))
def main(path):
    app = App(path)
    app.setup()

if __name__ == "__main__":
    main()