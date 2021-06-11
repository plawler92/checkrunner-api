import pytest

from tests.config import Config

@pytest.fixture
def config():
    return Config()