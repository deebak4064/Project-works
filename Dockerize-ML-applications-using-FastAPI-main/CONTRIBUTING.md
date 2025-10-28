# Contributing to Titanic Model API

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/titanic-model-api.git
cd titanic-model-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r titanic_model_api/requirements.txt
```

4. Install development dependencies:
```bash
pip install pytest pytest-cov black flake8 mypy
```

## Running Tests

```bash
pytest tests/
```

For coverage report:
```bash
pytest tests/ --cov=app --cov-report=html
```

## Code Style

We use:
- Black for code formatting
- Flake8 for style guide enforcement
- MyPy for type checking

Run formatting:
```bash
black .
flake8 .
mypy .
```

## Documentation

- Add docstrings to all public functions
- Follow Google style for docstrings
- Update README.md with any necessary changes

## Pull Request Process

1. Update the README.md with details of changes if applicable.
2. Update the requirements.txt if you add dependencies.
3. The PR will be merged once you have the sign-off of another developer.

## Any Questions?

Feel free to contact the project maintainers if you have any questions!