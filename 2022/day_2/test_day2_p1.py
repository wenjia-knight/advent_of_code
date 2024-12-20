import pytest
import unittest
from day2_p1 import check_who_wins

def test_who_wins():
    # GIVEN
    opponent_choice = 'A'
    your_choice = 'Y'

    # WHEN
    actual_outcome = check_who_wins(opponent_choice=opponent_choice, your_choice=your_choice)

    # THEN
    assert actual_outcome==expected_outcome