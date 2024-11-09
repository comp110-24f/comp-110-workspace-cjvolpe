"""Tests the function find_and_remove_max from find_max.py """

__author__ = "730773840"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:  # Checks for expected output
    a: list[int] = [10]
    assert find_and_remove_max(a) == 10


def test_find_and_remove_max_mutate() -> (
    None
):  # Checks that the list is mutated correctly
    b: list[int] = [1, 10, 2, 10, 381, -1]
    find_and_remove_max(b)
    assert b == [1, 10, 2, 10, -1]


def test_find_and_remove_max_edge() -> None:  # Checks for an edge case
    c: list[float] = [9, 9, 9, 9, 9, 9]
    assert find_and_remove_max(c) == 9 and c == []
