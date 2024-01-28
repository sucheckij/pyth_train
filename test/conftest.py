import pytest

# this is file visible for all test by Pytest during testing

@pytest.fixture
def input_value():
    n = 39
    return n