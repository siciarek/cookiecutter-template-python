from {{cookiecutter.project_pkg_name}}.lib.dummy import Dummy


def test_hello():
    assert Dummy().say_hello() == "Hello, World!"
    assert Dummy("Handsome").say_hello() == "Hello, Handsome!"
