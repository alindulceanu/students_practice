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


@pytest.mark.parametrize('x, y, result',[
    (1.6, 6, 9.6),
    (3.3, 19, 62.7)
])
@pytest.mark.product

def test_product(x,y,result):
    assert ob.product(x, y) == result


@pytest.mark.parametrize('x, y, result',[
    (5 ,9, 14),
    (59, 41, 100)
])

@pytest.mark.sum

def test_sum(x, y, result):
    assert ob.sum(x, y) == result

@pytest.mark.parametrize('x, y, result',[
    (5, 10, -5),
    (6, 15, -9)
])

def test_sub(x, y, result):
    assert ob.sub(x, y) == result

@pytest.mark.parametrize('x, y, result',[
    (7, 5, 1.4),
    (93, 7, 13.29)
])

@pytest.mark.divide
def test_divide(x, y, result):
    assert ob.divide(x, y) == result

@pytest.mark.skipif("sys.version > '3.11.0'")

def test_power():
    assert ob.power(5, 4) == 625
    assert ob.power(7, 3) == 343

