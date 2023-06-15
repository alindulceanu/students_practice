import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from practice import Calculations

import pytest


ob = None
def setup_module(module):
    global ob
    ob = Calculations()

@pytest.mark.parametrize('x, y, result',[
    (7, 5, 1.4),
    (93, 7, 13.29)
])

@pytest.mark.divide

def test_divide(x, y, result):
    assert ob.divide(x, y) == result