import pytest
from app.operations.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (1,2,3),
    (0,0,0),
    (-1,1,0),
    (-3,-7,-10),
    (1.5, 2.5, 4.0),
])

def test_add(a, b, expected):
    result=add(a, b)

    assert result==expected

@pytest.mark.parametrize("a, b, expected",[
    (10, 4, 6),
    (0, 0, 0),
    (-1, -1, 0),
    (5, 10, -5),
    (2.5, 1.0, 1.5),
])

def test_subtract(a, b, expected):
    result=subtract(a, b)

    assert result==expected

@pytest.mark.parametrize("a, b, expected",[
    (3, 4, 12),
    (0, 100, 0),
    (-2, 5, -10),
    (-3, -3, 9),
    (2.5, 4, 10.0),
])

def test_multiply(a, b, expected):
    result=multiply(a, b)

    assert result==expected

@pytest.mark.parametrize("a, b, expected",[
    (10, 2, 5),
    (9, 3, 3),
    (-10, 2, -5),
    (7, 2, 3.5),
])

def test_divide(a, b, expected):
    result=divide(a, b)

    assert result==expected

def test_divide_by_zero():
    
    a, b=10,0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a,b)

