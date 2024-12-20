import pytest
from p1 import is_special_char

@pytest.mark.parametrize("input", ["*", "$", "#"])
def test_is_special_char(input):
    given = input
    
    then = is_special_char(given)

    assert then == True 

@pytest.mark.parametrize("input", [".", "1"])
def test_is_not_special_char(input):
    given = input
    
    then = is_special_char(given)

    assert then == False