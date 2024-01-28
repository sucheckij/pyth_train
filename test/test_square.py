import math
import pytest

@pytest.mark.square
def test_srqrt():
    num = 25
    assert math.sqrt(num) == 25

@pytest.mark.square
def test_square():
    num = 7
    assert num*7 ==40

@pytest.mark.square
def test_quality():
    assert 11 == 10

@pytest.mark.other
def test_quality():
    assert 11 == 10