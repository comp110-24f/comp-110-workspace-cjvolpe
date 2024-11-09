"""List exercises"""

__author__ = "730773840"


def all(int_list: list[int], given_int: int) -> bool:
    """Determines if a list is all one number"""
    if len(int_list) == 0:  # List must have at least 1 number
        return False
    for (
        item
    ) in (
        int_list
    ):  # Iterates through the list and returns false if the list is not all one number
        if item != given_int:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Returns the largest integer in a list"""
    if len(int_list) == 0:  # list much have at least 1 value
        raise ValueError("max() arg is an empty list")
    max: int = int_list[0]
    for item in range(1, len(int_list)):  # Assigns max to the largest int in the list
        if max < int_list[item]:
            max = int_list[item]
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if two lists are equal"""
    if len(list_1) != len(list_2):  # The two lists must be the same length to be equal
        return False
    for item in range(
        0, len(list_1)
    ):  # Iterates through the second list and determines if it is equal to the first
        if list_1[item] != list_2[item]:
            return False
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends one list onto another"""
    for item in range(0, len(list_2)):  # Appends the first list to the second
        list_1.append(list_2[item])
