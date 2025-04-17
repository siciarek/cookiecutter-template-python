## Step 1: Install Cookiecutter

Install cookiecutter:

``` shell
brew install pipx
pipx install cookiecutter
pipx install pre-commit
pipx install licensecheck
```

or

``` shell
pip install cookiecutter
```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Run the following command and feed with answers, If you don’t know what to enter, stick with the defaults:

``` shell
pipx run cookiecutter git@github.com:siciarek/cookiecutter-template-python.git
```

Finally, a new folder will be created under current folder, the name is the answer you provided to `project_slug`.

Go to this generated folder, the project layout should look like:

```
.
├── .github
│   ├── dependabot.yml
│   └── workflows
│       └── gitleaks.yaml
├── .jenkins
│   └── Jenkinsfile
├── docs
│   ├── change-log.md
│   └── index.md
├── my_package
│   ├── __init__.py
│   └── entrypoints
│       └── hello.py
│   └── lib
│       └── dummy.py
└── tests
│   └── lib
│       └── test_dummy.py
├── .gitignore
├── .markdownlint.yaml
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

Here the project_slug is `my-package`, when you generate yours, it could be other name.

Also be noticed that there's `pyproject.toml` in this folder. This is the main configuration file of our project.

Do a first initial git commit. All pre-commit hooks should work without any problems.

```shell
# let's assume that for testing purposes for all the prompts You just press enter
cd python-template
git init
pre-commit install
git add .* *
git commit -a -m 'chore: initial commit'
```

Example output:
```
git commit -m "chore: initial commit"
nbstripout...........................................(no files to check)Skipped
bandit...................................................................Passed
pylint...................................................................Passed
ruff.....................................................................Passed
check yaml...............................................................Passed
check json...........................................(no files to check)Skipped
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
check python ast.........................................................Passed
check for case conflicts.................................................Passed
check for merge conflicts................................................Passed
pretty format json...................................(no files to check)Skipped
python tests naming..................................(no files to check)Skipped
fix utf-8 byte order marker..............................................Passed
debug statements (python)................................................Passed
trim trailing whitespace.................................................Passed
black....................................................................Passed
autoflake................................................................Passed
flake8...................................................................Passed
Dockerfile linter....................................(no files to check)Skipped
CRLF end-lines checker...................................................Passed
CRLF end-lines remover...................................................Passed
Pretty format YAML.......................................................Passed
docformatter.............................................................Passed
markdownlint.............................................................Passed
markdownlint-fix.........................................................Passed
type annotations not comments............................................Passed
[main (root-commit) 818d4db] chore: initial commit
```

## Step 3. Start use your new repo
Before changes in repo please check if all is working correctly.
``` shell
make install_dev
```

``` shell
make test
```

``` shell
make pipc
```

all commands should run without any problems.

## Step 4. Check documentation
Documentation will be published and available at `https://silenteight.github.io/{your_repo}` once:

If you'd like to see what it's look like now, you could run the following command:

``` shell
mkdocs serve
```

This will run the builtin development server for you to preview.
