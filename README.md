# tracker-tool

A short description of the project

---

[![PyPI Status](https://badge.fury.io/py/tracker_tool.svg)](https://pypi.org/project/tracker_tool/)
[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://Traenqui.github.io/tracker_tool/tracker_tool.html)
[![License](https://img.shields.io/github/license/Traenqui/tracker_tool)](https://github.com/Traenqui/tracker_tool/blob/main/LICENSE)
[![LastCommit](https://img.shields.io/github/last-commit/Traenqui/tracker_tool)](https://github.com/Traenqui/tracker_tool/commits/main)
[![Code Coverage](https://img.shields.io/badge/Coverage-0%25-red.svg)](https://github.com/Traenqui/tracker_tool/tree/main/tests)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://github.com/Traenqui/tracker_tool/blob/main/CODE_OF_CONDUCT.md)

Developers:

- Jonas Gerber (j.gerber2803@gmail.com)

## Setup

### Set up the environment

1. Run `make install`, which installs Poetry (if it isn't already installed), sets up a virtual environment and all Python dependencies therein.
2. Run `source .venv/bin/activate` to activate the virtual environment.

### Install new packages

To install new PyPI packages, run:

```
$ poetry add <package-name>
```

### Auto-generate API documentation

To auto-generate API document for your project, run:

```
$ make docs
```

To view the documentation, run:

```
$ make view-docs
```

## Tools used in this project

- [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management
- [hydra](https://hydra.cc/): Manage configuration files
- [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting
- [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project

## Project structure

```
.
├── .flake8
├── .github
│   └── workflows
│       ├── ci.yaml
│       └── docs.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── config
│   ├── __init__.py
│   └── config.yaml
├── data
├── makefile
├── models
├── notebooks
├── poetry.toml
├── pyproject.toml
├── src
│   ├── scripts
│   │   ├── fix_dot_env_file.py
│   │   └── versioning.py
│   └── tracker_tool
│       └── __init__.py
└── tests
    └── __init__.py
```
