import pytest

@pytest.fixture
def input_value():
    n = 39
    return n

def test_divisibility_by_3(input_value):
    assert input_value % 3 == 0

def test_divisibility_by_6(input_value):
    assert input_value % 6 == 0