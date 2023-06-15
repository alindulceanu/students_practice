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

@pytest.mark.parametrize('x, y, result',[
    (5 ,9, 14),
    (59, 41, 100)
])

@pytest.mark.sum

def test_sum(x, y, result):
    assert ob.sum(x, y) == result