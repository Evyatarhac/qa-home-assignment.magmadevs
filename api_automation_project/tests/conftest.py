import pytest
from utils.auth import generate_token

@pytest.fixture(scope="session")
def token():
    """Generate token once per test session."""
    return generate_token()
