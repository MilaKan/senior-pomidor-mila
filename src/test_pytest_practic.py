

from calculator import sum
def test_sum():
    assert sum(3,4) ==7
    assert sum(2, 3) == 5
    assert sum(1, -1) == 0
    assert sum(-1, -1) == -2