import pytest
from day_06.p1 import ways_to_win

@pytest.mark.parametrize(argnames=["input_1", "input_2", "expected"], argvalues=[(7,9, 4), (15,40, 8),(30,200, 9)])
def test_ways_to_win(input_1, input_2, expected):
    given = expected

    then = ways_to_win(input_1, input_2)

    assert then == given