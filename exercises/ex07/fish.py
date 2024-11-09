"""File to define Fish class."""

__author__ = "730773840"


class Fish:
    """Blueprint for a fish object."""

    age: int

    def __init__(self):
        """Instantiates a fish object."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates one day in a fish's life."""
        self.age += 1
        return None
