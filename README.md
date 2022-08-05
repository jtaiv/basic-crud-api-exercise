# Master Class Data Platform API Exercise

A starter project for HTTP API creation exercise. The exercise uses `Python` and `FastAPI` framework to build a working HTTP API. Documentation to the framework can be found in [FastAPI](https://fastapi.tiangolo.com/). The Framework uses similar interface as `Flask` but with more enhanced features like out of the box OpenAPI documentation.


## Requirements

To run this exercise, you need the Visual Studio Code (VSCode), Python 3.9 or higher and a browser. Additionally, you will need poetry pip package. After you have a functional Python installation, you can just write in terminal of your choice

```bash
python --version  # To validate the version and installation
python -m pip install poetry
```


## Local Setup

First open the repository in VSCode and its terminal. Make sure the Terminal points to this project folder. Then install the packages

```bash
poetry install
```

This should create a virtual environment for you automatically, note from the command output where it is stored. You can enable the virtual environment from poetry by

```bash
poetry shell
```

Now you should be ready to continue the exercise. The server can be run with the command

```bash
uvicorn internal_mcdp.main:app --reload
```
