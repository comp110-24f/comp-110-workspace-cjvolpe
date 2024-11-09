"""Summing elements of a list using different loops"""

__author__ = "730773840"


def w_sum(vals: list[float]) -> float:
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for val in range(0, len(vals)):
        sum += vals[val]
    return sum
