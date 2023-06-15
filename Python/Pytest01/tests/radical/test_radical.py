import sys
from mathematic import radical
import pytest


@pytest.mark.parametrize(
    "x, y",
    [
        (4, 2),
        pytest.param(1, 0, marks=pytest.mark.xpass),
        pytest.param(1249, 1000, marks=pytest.mark.xfail(reason="NU VREAU")),
        (7, 3),
        (25, 5),
        (9, 3),
        pytest.param(10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")),
    ],
)
def test_radical(x, y):
    assert radical(x) == y
