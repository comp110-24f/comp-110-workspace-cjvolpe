"""File to define Bear class."""

__author__ = "730773840"


class Bear:
    """Blueprint for a bear  objects."""

    age: int
    hunger_score: int

    def __init__(self):
        """Instantiates a bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates one day in a bear's life."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Simulates a bear eating."""
        self.hunger_score += num_fish
