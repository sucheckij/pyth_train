import pytest

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.skip # skipuje test
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.other
def test_less():
    num = 100
    assert num < 100



