"""Tea Party Planner program"""

__author__: str = "730773840"


def main_planner(
    guests: int,
) -> None:  # Prints the plan for the tea party using the previous functions
    """Plan a tea party for any number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calcualtes the number of tea bags needed based on attendees"""
    return 2 * people  # each person drinks two bags of tea


def treats(people: int) -> int:
    """Calculate the number of treats based on number of tea bags"""
    return int(
        1.5 * tea_bags(people=people)
    )  # number of treats needed in 1.5x the number of teabags


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of hosting a tea party"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # total cost = # of tea bags * cost of tea bags + # of treats* cost of treats


if __name__ == "__main__":  # Gets the number of guests attending the tea party
    main_planner(guests=int(input("How many guests are attending your tea party?\n")))
