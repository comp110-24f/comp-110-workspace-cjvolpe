from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Unit tests for utils.py"""

__author__ = "730773840"


def test_only_evens_use() -> None:
    """Test to see if the function gives the expected output"""
    a: list[int] = [1, 2, 3, 4, 5, 6]  # Test lsit
    assert only_evens(a) == [2, 4, 6]  # Should return the evens from the list


def test_only_evens_mut() -> None:
    """Test to see if the function does not mutate the list"""
    a: list[int] = [1, 2, 3]  # Test List
    only_evens(a)
    assert a == [1, 2, 3]  # The list should not be mutated


def test_only_evens_edge() -> None:
    """Test to see if the function can deal with an unexpected input"""
    a: list[int] = []  # Empty list
    assert only_evens(a) == list()  # Should return an empty list


def test_sub_use() -> None:
    """Tests for expected output from the function"""
    a: list[int] = [1, 2, 3, 4, 5]  # Test list
    assert sub(a, 1, 3) == [
        2,
        3,
    ]  # Should return the elements from index 1, not including index 3


def test_sub_mut() -> None:
    """Tests to see if the function does not mutate the function"""
    a: list[int] = [1, 2, 3, 4, 5]  # Test List
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4, 5]  # The list should not be mutated


def test_sub_edge() -> None:
    """Tests for an unexpected input"""
    a: list[int] = [1, 2, 3, 4, 5]  # Test list
    assert sub(a, -1, 3) == [
        1,
        2,
        3,
    ]  # If the start is negative, start at the beginning


def test_add_at_index_use() -> None:
    """Tests for the expected output"""
    a: list[int] = [1, 2]  # Test list
    assert add_at_index(a, 3, 2) is None  # The function should output Nothing


def test_add_at_index_mut() -> None:
    """Tests to see if the function mutates the list properly"""
    a: list[int] = [1, 3, 9]  # Test list
    add_at_index(a, 5, 2)
    assert a == [1, 3, 5, 9]  # Should add the int 3 at index 2


def test_add_at_index_edge() -> None:
    """Tests for an unexpected input"""
    a: list[int] = [6, 6, 8]  # Test list
    with pytest.raises(IndexError):  # The function should raise an IndexError
        add_at_index(a, 0, 4)
