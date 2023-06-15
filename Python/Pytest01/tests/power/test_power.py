from mathematic import power
import pytest

@pytest.mark.parametrize(
    'x, y, z',
    (
        (2, 2, 4),
        (6, 3, 50),
        (3, 3, 27),
        (2, 4, 8),
        (5, 8, 125),
        (7, 4, 6),
    )
)
def test_power(x, y, z):
    assert power(x, y) == z
