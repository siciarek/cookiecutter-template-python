import click
from {{cookiecutter.project_pkg_name}}.lib.dummy import Dummy


@click.command()
@click.option("-n", "--name", type=str, default="World")
def main(name: str):
    message = Dummy().say_hello(name=name)
    click.echo(message=message)
