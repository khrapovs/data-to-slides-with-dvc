# From raw data to management slides with DVC

![CI](https://github.com/khrapovs/data-to-slides-with-dvc/actions/workflows/workflow.yaml/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
## Usage

Create virtual environment:
```shell
uv venv
```
Install dependencies:
```shell
uv sync --all-extras
```
Run DVC pipeline:
```shell
dvc repro -R dvc
```

## Contribute

Create virtual environment:
```shell
uv venv
```
Install dependencies:
```shell
uv sync --all-extras
```
Install pre-commit:
```shell
pre-commit install
```
