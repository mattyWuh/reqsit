# Reqsit

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A CLI tool for converting requirements.txt entries to a form accepted by pyproject.toml.
Pronounced "RECKS-IT".

## Getting started.

Install `reqsit` with `pip`,

```
pip install --user reqsit
```

Run by executing the command from the root folder of your project,

```
reqsit
```

If you prefer to use a name other than `requirements.txt` for your requirements file, then add a `--filename` argument.
For example, to use the file `foo.bar`, enter

```
reqsit --filename=foo.bar
```

## How to contribute.