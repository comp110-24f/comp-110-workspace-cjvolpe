"""Function that finds and removes the max value of a list"""

__author__ = "730773840"


def find_and_remove_max(input: list[int]) -> int:
    """Find the largest item in a list and removes all instances"""
    max_idx: int = -1

    if len(input) == 0:  # Exits function if the list is empty
        return max_idx

    max: int = input[0]

    for idx in range(1, len(input)):  # Identifies max value
        if input[idx] > max:
            max = input[idx]
            max_idx = idx

    critical_points: list[int] = []

    for idx in range(
        len(input) - 1, -1, -1
    ):  # Iterates through the list backwards to make a backwards list
        # Done to ensure that only the correct values are removed
        if input[idx] == max:
            critical_points.append(idx)

    for point in critical_points:  # Removes all instances of the max value
        input.pop(point)

    return max
