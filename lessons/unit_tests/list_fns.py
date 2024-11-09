"""Three important functions for class on 10/14"""

__author__ = "730773840"


def get_first(input_list: list[str]) -> str:
    """Return first element"""
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Remove first element"""
    input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Return and remove first element"""
    return input_list.pop(0)
