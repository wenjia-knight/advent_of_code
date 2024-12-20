import pytest
from day_07.p1 import *

@pytest.mark.parametrize(
    argnames=["input", "expected"], argvalues=[("AAAAA", True), ("32T3K", False)]
)
def test_is_five_a_kind_true(input, expected):
    given = expected
    then = is_five_of_a_kind(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"], argvalues=[("AAAAA", False), ("AA8AA", True)]
)
def test_is_four_a_kind_true(input, expected):
    given = expected
    then = is_four_of_a_kind(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("48488", True), ("ABABS", False), ("AAAAB", False)]
)
def test_is_full_house(input, expected):
    given = expected
    then = is_full_house(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("TTT98", True), ("48488", False), ("ABABS", False), ("ABCDE", False)],
)
def test_is_three_of_a_kind(input, expected):
    given = expected
    then = is_three_of_a_kind(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("TTT98", False), ("48488", False), ("ABABS", True), ("22353", True)],
)
def test_is_two_pair(input, expected):
    given = expected
    then = is_two_pair(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("T1298", False), ("48488", False), ("ABABS", False), ("22354", True)],
)
def test_is_one_pair(input, expected):
    given = expected
    then = is_one_pair(input)
    assert then == given


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("T1298", True), ("48488", False), ("ABA35", False), ("22354", False)],
)
def test_is_high_card(input, expected):
    given = expected
    then = is_high_card(input)
    assert then == given

@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[("23456", 1), ("A23A4", 2), ("23432", 3), ("TTT98", 4), ("48488", 5), ("AA8AA", 6), ("AAAAA", 7)]
)
def test_check_hand_type(input, expected):
    given = expected
    then = check_hand_type(input)
    assert then == given