import click
from {{cookiecutter.project_pkg_name}}.container import Ioc
from {{cookiecutter.project_pkg_name}}.lib.dummy import Dummy


@click.command()
@click.option("-n", "--name", type=str, default="World")
def main(name: str):
    Ioc.logger().debug("START")
    message = Dummy(name=name).say_hello()
    click.echo(click.style(message, fg="green", reverse=True))
    Ioc.logger().debug("END")