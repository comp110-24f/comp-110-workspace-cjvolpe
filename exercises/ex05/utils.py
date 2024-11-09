"""Functions for testing in utils_test.py"""

__author__ = "730773840"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list of even integers from"""
    even_list: list[int] = list()
    for num in input:  # For each number in the list, check if odd
        if num % 2 == 0:  # If odd add to a list of even numbers
            even_list.append(num)
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Outputs a new list of ints based on the set range"""
    sub_list: list[int] = list()
    if (
        len(input) == 0 or start > end or end <= 0
    ):  # If the list is empty, start is greater than end or end is zero
        # Return empty list
        return sub_list
    if end > len(
        input
    ):  # Set the end to the length of the list if original end is to large
        end = len(input)
    if start < 0:  # If start is negative, set start to the start of the list
        start = 0
    for idx in range(
        start, end
    ):  # Create a list of ints from original list between the range
        sub_list.append(input[idx])
    return sub_list


def add_at_index(input: list[int], new_int: int, index: int) -> None:
    """Adds a new int an index and shifts the rest of the list right"""
    if (
        index > len(input) or index < 0
    ):  # Int can be added to the end of the list but no further
        raise IndexError("Index is out of bounds for the input list")
    if index == len(input):  # Append new_int if there are no ints after the index
        input.append(new_int)
    else:
        input.append(42)  # Increase the size of the list by 1
        for idx in range(len(input) - 1, index, -1):  # Starts at the end of the list
            input[idx] = input[idx - 1]  # Assigns the element to the element in front
        input[index] = new_int
