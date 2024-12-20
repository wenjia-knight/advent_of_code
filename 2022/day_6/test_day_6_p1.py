import pytest
from day_6_p1 import find_character

TEST_INPUT = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
def test_find_character():
    # GIVEN
    expected_outcome = 5

    # WHEN
    actual_outcome = find_character(a_list=list(TEST_INPUT))

    # THEN
    assert expected_outcome == actual_outcome