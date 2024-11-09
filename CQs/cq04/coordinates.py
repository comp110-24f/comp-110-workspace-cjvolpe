"""Function that iterates through two strings and prints each index as a coord"""

__author__ = "730773840"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):  # Changes the x value so the ys can be iterated through
        while idx2 < len(ys):  # Iterates through the y values and keeps x constant
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 += 1
        idx1 += 1
        idx2 = 0
