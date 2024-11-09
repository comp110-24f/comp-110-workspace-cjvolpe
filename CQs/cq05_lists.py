"""Mutating Lists"""

__author__ = "730773840"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(user_list: list[int], user_num: int) -> None:
    user_list.append(user_num)


def double(user_list: list[int]) -> None:
    idx: int = 0
    while idx < len(user_list):
        user_list[idx] *= 2
        idx += 1


double(list_2)

print(list_1)
print(list_2)
