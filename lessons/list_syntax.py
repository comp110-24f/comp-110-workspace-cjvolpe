"""List practice"""

my_numbers: list[float] = []  # Literal
my_numbers: list[float] = list()  # Constructor

my_numbers.append(1.5)  # Adds a value to the end of a list
my_numbers.append(2.5)

# print(my_numbers)

game_points: list[int] = [102, 86, 94]

# [int | float]

print(game_points)

# Subscription Notation
print(game_points[2])
print([1, 2, 3][1])

# Modifying by Index
# (Because lists are mutable)
game_points[1] = 72


# List length
print(len(game_points))

# Remov items from list
print(game_points)
game_points.pop(1)
print(game_points)

# Practice


def display(int_list: list[int]) -> None:
    """Displays the values of int_list"""
    idx: int = 0
    while idx < len(int_list):
        print(int_list[idx])
        idx += 1


display(int_list=game_points)
