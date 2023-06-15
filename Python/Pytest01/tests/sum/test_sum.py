from mathematic import sum
import pytest

@pytest.mark.sum
def test_sum():
    assert sum(2,3) == 5