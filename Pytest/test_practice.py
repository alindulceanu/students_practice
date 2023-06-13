from practice import Calculations
import pytest

ob = None
def setup_module(module):
    global ob
    ob = Calculations()

@pytest.mark.parametrize("x, y, result",
                         [
                             (69, 2, 8.31),
                             (795, 7, 2.6)
                         ])
def test_xRoot(x, y, result):
    assert ob.xRoot(x, y) == result


@pytest.mark.parametrize('x, y, result',[
    (1.6, 6, 9.6),
    (3.3, 19, 62.7)
])
def test_product(x,y,result):
    assert ob.product(x, y) == result

def test_sum():
    assert ob.sum(5,9) == 14
    assert ob.sum(59, 41) == 100

def test_sub():
    assert ob.sub(5, 10) == -5
    assert ob.sub(6, 15) == -9

def test_divide():
    assert ob.divide(7, 5) == 1.4
    assert ob.divide(93, 7) == 13.29

def test_power():
    assert ob.power(5, 4) == 625
    assert ob.power(7, 3) == 343