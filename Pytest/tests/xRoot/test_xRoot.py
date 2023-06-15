import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)


import pytest
from practice import Calculations

ob = None
def setup_module(module):
    global ob
    ob = Calculations()

@pytest.mark.parametrize("x, y, result",
                         [
                             (69, 2, 8.31),
                             (795, 7, 2.6)
                         ])

@pytest.mark.xRoot

def test_xRoot(x, y, result):
    assert ob.xRoot(x, y) == result