from mathematic import radical_ordin
import pytest


@pytest.mark.skip()
def test_radical_ordin():
    assert radical_ordin(1296, 4) == 6