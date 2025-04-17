from dependency_injector import containers, providers

from {{cookiecutter.project_pkg_name}}.logger import Logger
from {{cookiecutter.project_pkg_name}} import settings

# pylint: disable=too-few-public-methods
class Ioc(containers.DeclarativeContainer):
    """Services provider class (Dependency Injection)."""

    logger = providers.Singleton(
        Logger,
        name=settings.APP_SHORT_NAME,
        level=settings.LOG_LEVEL,
        fmt="%(asctime)s.%(msecs)03d %(levelname)s THREAD:%(threadName)s %(name)s - %(module)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
