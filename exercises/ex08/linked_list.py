"""EX08 Recursion Exercises w/ a linked list."""

from __future__ import annotations

__author__ = "730773840"


class Node:
    """Class of a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Creates a linked list object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = str()
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Finds that value at a certain index in a linked list."""
    if index < 0 or head is None:  # Edge case: index too large or value_at empty
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # Base Case: Value at index 0
        return head.value
    return value_at(
        head.next, index - 1
    )  # Increments towards index zero in order to reach a base case


def max(head: Node | None) -> int:
    """Find the max value in a linked list."""
    if head is None:  # Cannot find the max of an empty list
        raise ValueError("Cannot call max with None.")
    if head.next is None:  # End of the list / 1 element
        return head.value
    if head.value >= max(
        head.next
    ):  # Find if current value is great than what is left in the list
        return head.value
    else:  # If it is not greater, find the greatest value of what is left (i+= 1)
        return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list given a list."""
    if len(items) == 0:  # Base Case: list becomes empty or is empty
        return None
    return Node(
        items[0], linkify(items[1:])
    )  # Creates Node objects using the first element and assigns node.next


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales a linked list by a factor."""
    if head is None:  # Base Case: end of list / list is empty
        return None
    return Node(
        head.value * factor, scale(head.next, factor)
    )  # Scales head and puts the rest of this in a recursive statement
