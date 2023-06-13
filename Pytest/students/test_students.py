from funny import studentDB
import pytest
import sys

db = None
@pytest.fixture(scope = 'module')
def db():
    print('---------setup---------')
    global db
    db = studentDB()
    db.connect('data.json')
    yield db
    db.close()
    print('-----teardown-----')


'''def setup_module(module):
    global db
    db = studentDB()
    db.connect('data.json')    

def teardown_module(module):
    db.close()'''


@pytest.mark.parametrize('arg, result',
                         [
                             ('id', 1),
                             ('name', 'Scott'),
                             ('result', 'pass')
                         ])
def testScottData(db, arg, result):
    scottData = db.getData('Scott')
    assert scottData[arg] == result
    
@pytest.mark.parametrize('arg, result',
                         [
                             ('id', 2),
                             ('name', 'Mark'),
                             ('result', 'fail')
                         ])
def testMarkData(db, arg, result):
    markData = db.getData('Mark')
    assert markData[arg] == result