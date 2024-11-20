from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(str(courses))
print(courses)
# Be sure to get here!


def to_str(head: Node | None) -> str:
    """Represents a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    if head.next is None:
        # Base Case: when head is the last node
        return head.value
    else:
        # Recurseive case:
        return last(head.next)


print(last(one))  # Expect to print 2
print(last(courses))  # Expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end"""
    if start == end:
        return None
    if start > end:
        raise ValueError("Invalid arguments, start > end")
    # 1. Handle the first value in your new list here:
    first: int = start
    # 2. Let the rest of the list be handled recursively!
    rest: Node | None = recursive_range(start + 1, end)
    # 3. Return a new node which is first followed by rest
    return Node(first, rest)


r_list: Node | None = recursive_range(110, 113)
print(r_list)
