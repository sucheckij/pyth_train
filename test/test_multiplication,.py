import pytest

@pytest.mark.parametrize('num, output',[(1,11), (2,22), (3,33), (4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output


@pytest.mark.parametrize('numt',[1,2,3,4])
@pytest.mark.parametrize('output',[11,22,33,44])
def test_multiplication_11(num, output):
    assert 11 * num == output