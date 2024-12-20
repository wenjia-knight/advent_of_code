import pytest
from day_6_p2 import find_character

TEST_INPUT = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
def test_find_character():
    # GIVEN
    expected_outcome = 19

    # WHEN
    actual_outcome = find_character(a_list=list(TEST_INPUT))

    # THEN
    assert expected_outcome == actual_outcome