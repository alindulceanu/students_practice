from mathematic import minus
import pytest

@pytest.mark.parametrize(
    'x, y, z',
    (
        (5, 2, 3),
        (8, 4, 2),
    )
)
def test_minus(x, y, z):
    assert minus(x, y) == z