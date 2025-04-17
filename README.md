# cookiecutter-python-template
Cookiecutter Template Repository for Your Python applications.

## Quickstart

Install the latest [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) if you haven't installed it yet (this requires Cookiecutter 2.6.0 or higher):

You can install Cookiecutter as `pip` or [pipx](https://pipx.pypa.io/stable/) installation.

```shell
# pipx is strongly recommended.
brew install pipx
pipx install cookiecutter
```

```shell
# If pipx is not an option,
python -m pip install cookiecutter
```

Generate a Python package project:

```shell
pipx run cookiecutter git@github.com:siciarek/cookiecutter-python-template.git
```

Then follow **[Tutorial](docs/getting-started.md)** to finish other configurations.

## Features

This tool will create Python project with the following features:

* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Check static type with [Mypy](http://mypy-lang.org/) (optional)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

## NFRs

Template include all NFR mandatory setup, please use this template for each new python development. 

Detailed description about NFRs can be found below:

* [Python Code Style Guide](https://silent8.atlassian.net/wiki/spaces/AB/pages/916193373/Python+Code+Style+Guides+NFR-165) ([NFR-165](https://silent8.atlassian.net/browse/NFR-165))
* [Python Static File Check (include code formatting)](https://silent8.atlassian.net/wiki/spaces/AB/pages/915800322/Python+Static+File+Check+include+code+formatting+NFR-166) ([NFR-166](https://silent8.atlassian.net/browse/NFR-166))
* [Python Mandatory files in Repo / Python Repo template / Project Dev Documentation](https://silent8.atlassian.net/wiki/spaces/AB/pages/915603739/Python+Mandatory+files+in+Repo+Python+Repo+template+Project+Dev+Documentation+NFR-167) ([NFR-167](https://silent8.atlassian.net/browse/NFR-167))
* [Codebase Security Scans](https://silent8.atlassian.net/wiki/spaces/AB/pages/457244695/Codebase+Security+Scans+NFR-64) ([NFR-64](https://silent8.atlassian.net/browse/NFR-64))
* [Python Security - Bandit](https://silent8.atlassian.net/wiki/spaces/AB/pages/915407149/Python+Security+-+Bandit+NFR-169) ([NFR-169](https://silent8.atlassian.net/browse/NFR-169))
* [Python Build Process](https://silent8.atlassian.net/wiki/spaces/AB/pages/915996759/Python+Build+Process+NFR-168) ([NFR-168](https://silent8.atlassian.net/browse/NFR-168))

---

The **cookiecutter-python-template** documentation was constructed using [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

Source of this documentation can be found in [docs](docs) folder.
