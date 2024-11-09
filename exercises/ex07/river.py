"""File to define River class."""

__author__ = "730773840"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creates a river ecosystem and simulates it."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages and removes old fish & bears."""
        living_fish: list[Fish] = list()
        living_bears: list[Bear] = list()

        for fish in self.fish:  # Adds living fish to a list
            if fish.age <= 3:
                living_fish.append(fish)

        for bear in self.bears:  # Adds living bears to a list
            if bear.age <= 5:
                living_bears.append(bear)

        self.bears = living_bears  # Saves living bears, removing the old ones
        self.fish = living_fish  # Saves living fish, removing the old ones

        return None

    def bears_eating(self):
        """Simulates bears eating fish."""
        for bear in self.bears:  # Simulates for every bear
            if len(self.fish) >= 5:  # If there are enough fish
                bear.eat(3)  # Each bear eats 3 fish
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Simulates hunger."""
        living_bears: list[Bear] = list()
        for bear in self.bears:  # Adds bears with enough hunger_score toa list
            if bear.hunger_score >= 0:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        """Simulates fish reproduction."""
        if len(self.fish) >= 2:
            for fish in range(
                0, (len(self.fish) // 2) * 4
            ):  # For every 2 fish, 4 are produced
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Simualtes bear reproduciton."""
        if len(self.bears) >= 2:
            for bear in range(
                0, len(self.bears) // 2
            ):  # For every 2 bears, 1 is produced
                self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints a report on the river every day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week in the river."""
        day: int = 1
        while day <= 7:
            self.one_river_day()
            day += 1

    def remove_fish(self, amount: int) -> None:
        """Removes fish from self.fish."""
        for num_fish in range(0, amount):
            self.fish.pop(num_fish)
