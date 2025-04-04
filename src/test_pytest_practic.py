

#from calculator import add
from calculator import add
def test_add():
    assert add(3,4) ==7
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(-1, -1) == -2