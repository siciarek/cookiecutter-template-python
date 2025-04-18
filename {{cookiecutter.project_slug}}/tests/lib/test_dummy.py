import pytest
from {{cookiecutter.project_pkg_name}}.lib.dummy import Dummy


hello_data_provider = (
    (None, "Hello, World!", "No constructor args."),
    ("Handsome", "Hello, Handsome!", "Custom name: Handsome."),
    ("Gorgeous", "Hello, Gorgeous!", "Custom name: Gorgeous."),
)

@pytest.mark.parametrize("name, expected, message", hello_data_provider)
def test_hello(name, expected, message):
    srv = Dummy(name=name) if name else Dummy()
    assert srv.say_hello() == expected, message
