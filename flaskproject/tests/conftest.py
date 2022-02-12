import pytest
from src.app import create_app


# python -m pytest tests/ --fixtures
# pytests < alias = python -m pytest tests/ -v
# pytestscov < alias = python -m pytest tests/ -v --cov=flaskproject
# startindex < alias = start "Google Chrome" htmlcov/index.html
# flask shell < python -m flask shell
@pytest.fixture(scope="function")
def app():
    """Instance of Main Flask App"""
    return create_app()