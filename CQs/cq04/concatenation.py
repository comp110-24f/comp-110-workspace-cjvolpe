"""Function that concatenates two strings"""

__author__ = "730773840"


def concat(string1: str, string2: str) -> str:  # Combines string1 and string2
    return string1 + string2


concat("hello", "world")

word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
