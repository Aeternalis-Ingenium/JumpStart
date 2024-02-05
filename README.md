# API Application Template

<p align="center">
    <a href="https://app.codecov.io/gh/Aeternalis-Ingenium/JumpStart/tree/trunk" >
        <img src="https://codecov.io/gh/Aeternalis-Ingenium/JumpStart/graph/badge.svg?token=qSZUkjga7N"/>
    </a>
    <a href="https://results.pre-commit.ci/latest/github/Aeternalis-Ingenium/JumpStart/trunk">
        <img src="https://results.pre-commit.ci/badge/github/Aeternalis-Ingenium/JumpStart/trunk.svg" alt="pre-commit.ci status">
    </a>
    <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
    </a>
    <a href="https://pycqa.github.io/isort/">
        <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="Imports: isort">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/mypy-checked-blue" alt="mypy checked">
    </a>
    <a href="https://github.com/Aeternalis-Ingenium/JumpStart/actions/workflows/ci.yaml">
        <img src="https://github.com/Aeternalis-Ingenium/JumpStart/actions/workflows/ci.yaml/badge.svg" alt="Continuous Integration">
    </a>
    <a href="https://github.com/Aeternalis-Ingenium/JumpStart/blob/trunk/LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    </a>
    <a href="https://github.com/Aeternalis-Ingenium/JumpStart/blob/trunk/README.md">
        <img src="https://img.shields.io/badge/docs-passing-brightgreen.svg" alt="Documentation">
    </a>
</p>

This template is created to jump-start your API development by providing the setup from a real-world project! This template utilizes the following tech stack:

* 🐍 [Python](https://www.python.org/) v3.12.1 or higher.
* ⚡️ [FastAPI](https://fastapi.tiangolo.com/) as the main web framework.
* 🦄 [Uvicorn](https://www.uvicorn.org/) for the web server.
* 🐳 [Docker](https://www.docker.com/) for containerization.
* 🐙 [GitHub Actions](https://docs.github.com/en/actions) for the CI.

### URLs

With your localhost, you can find all endpoints after the `api/` prefix. The first page is the api health checker to show you if your server is running properly.

* API health checker $˜\rightarrow$ `http://localhost:8000/api/`.
* API Documentation $˜\rightarrow$ `http://localhost:8000/docs/`.

with Docker, you just change the host into `0.0.0.0`:

* API health checker $˜\rightarrow$ `http://0.0.0.0:8000/api/`.
* API Documentation $˜\rightarrow$ `http://0.0.0.0:8000/docs/`.

## Why the above Tech-Stack?

Lean speed!

* FastAPI is crowned as the fastest web framework for Python and thus we use it for our backend development.

* Uvicorn fills the gap for low-level server/application interface for Python's asynchronous frameworks such as FastAPI.

* Docker is a technology that packages an application into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

* GitHub Actions provide a comprehensive method to setup our continuous integration and deployment.

## Other Stacks

There are other technologies utilized in this project template to ensure that your application is robust and provides the best possible development environment for your team!

* [TOML](https://toml.io/en/) $\rightarrow$ It provides a signle source of configuration for your project!
* [PyEnv](https://github.com/pyenv/pyenv) $\rightarrow$ The simplest way to manage our Python version.
* [Pyenv-VirtualEnv](https://github.com/pyenv/pyenv-virtualenv) $\rightarrow$ The plugin for `Pyenv` to manage the virtual environment for our packages.
* [Pre-Commit](https://pre-commit.com/) $\rightarrow$ Git hook scripts to identify issues and quality of your code before pushing it to GitHub.
* [Pre-Commit CI](https://pre-commit.ci/) $\rightarrow$ Continuous integration for our Pre-Commit hook that fixes and updates our hook versions.
* [Black (Python)](https://black.readthedocs.io/en/stable/) $\rightarrow$ Manage your Python code style with auto-formatting.
* [Isort (Python)](https://pycqa.github.io/isort/) $\rightarrow$ Sort your `import` for clarity. Also for Python.
* [MyPy (Python)](https://mypy.readthedocs.io/en/stable/) $\rightarrow$ A static type checker for Python that helps you to write cleaner code.
* [PyTest](https://docs.pytest.org/en/7.2.x/) $\rightarrow$ The testing framework for Python code.
* [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) $\rightarrow$ A file for distributing the responsibilities in our project to each team/teammate.
* [CodeCov](https://about.codecov.io/) $\rightarrow$ A platform that analyzes the result of your software tests.

## Setup Guide

There are 2 ways to develop your project. The first way is with your local environment. This is totally fine but it would be quite complex if youh have a bigger team where everyone uses a different operating system. Hence I prepare the Docker scripts in `docker/` that you can execute so everyone will use the same operating system that is defined in the Docker virtual machine (container) via my script. Both ways will be prepared in the following steps:

1. Python project setup:
    ```shell
    # Creating VENV
    pyenv virtualenv 3.12.1 <YOUR_ENV_NAME>
    pyenv local <YOUR_ENV_NAME>

    # Install dependencies
    pip3 install -r requirements.txt

    # Test run your backend server
    uvicorn src.main:app --reload
    ```

2. Testing with `PyTest`:
   ```shell
   # For testing without Docker
   pytest -vv

   # For testing within Docker
   docker exec app pytest -vv
   ```

3. `Pre-Commit` setup:
    ```shell
    # Make sure you are in the ROOT project directory
    pre-commit install
    pre-commit autoupdate

    # To execute
    pre-commit run
    ```

4. Credentials setup:
    If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template are located in `.env.example`.

    If you want to have another name for the secret variables, don't forget to change them also in:

    * `.github/workflows/ci.yaml`
    * `backend/src/config.py`
    * `docker-compose.yaml`

    ```shell
    # Make sure you are in the ROOT project directory
    touch .env

    echo "SECRET_VARIABLE=SECRET_VARIABLE_VALUE" >> .env
    ```

5. `CODEOWNERS` setup:
    Go to `.github/` and open `CODEOWNERS` file to assign any type of tiles to your team members.

6. Docker setup:
   ```shell
    docker-compose build
    docker-compose up

    # Every time you write a new code, update your container with:
    docker-compose up -d --build
   ```

7. Go to https://about.codecov.io/, and sign up with your github to get the `CODECOV_TOKEN` for your repository.

8.  Go to your GitHub repository and register all the credentials in `.env.example` repository settings (`settings` $\rightarrow$ (scroll down a bit) `Secrets` $\rightarrow$ `Actions` $\rightarrow$ `New repository secret`)

## Project Structure

```shell
├── .github/
    ├── ISSUE_TEMPLATE/         # Directory for collaboration templates.
        ├── bug_report.md       # Module to follow when reporting bugs.
        ├── feature_request.md  # Module to follow when requesting features.
    ├── workflows/              # Directory for continuous operations: CI/CD.
        ├── ci.yaml             # Module for CI.
    ├── CODEOWNERS              # Module to distribute code ownership.
├── coverage/                   # Directory for test coverage reports.
├── docker/
    ├── docker-compose.yaml     # Module for docker compose.
    ├── Dockerfile.dev          # Module for docker container in development.
    ├── Dockerfile.prod         # Module for docker container in production.
├── src/
    ├── api/
        ├── routes/             # Directory for routes.
            ├── api_health.py   # Module for API health checker.
        ├── endpoints.py        # Module for all routes.
    ├── core/
        ├── config.py           # Module for application settings.
        ├── events.py           # Module for in-app event registration.
        ├── logger.py           # Module for custom logging system.
    ├── models/
        ├── domain/             # Directory for all domain models.
        ├── schema/             # Directory for schema models.
            ├── base.py         # Module with base class for schema models.
    ├── utils/
        ├── formatter.py        # Module with formatters.
    ├── main.py                 # Module with application class.
├── tests/
    ├── integration_tests/      # Directory for integration tests.
        ├── routes/             # Directory for testing all routes.
            ├── api_health_py   # Module that tests health checker endpoint.
    ├── unit_tests/             # Directory for unit tests.
        ├── test_src_version.py # Module that tests the `src/` version.
    ├── conftest.py             # Module for test configuration.
├── .dockerignore               # Module with docker ignore list.
├── .env.example                # Module with secret names (rename to .env).
├── .gitignore                  # Module with git ignore list.
├── .pre-commit-config.yaml     # Module for safeguarding commit message.
├── LICENSE.md                  # Module with license type (to be deleted).
├── codecov.yaml                # Module for Codecov configuration.
├── pyproject.toml              # Module for project configuration.
├── README.md                   # Module for project documentation.
├── requirements.txt            # Module with python packages.
```

## Thank You!

Happy engineering and never stop innovating! For feedback, bug reports, or feature requests, please use the issue template and create an issue so we can tackle it as a community!
