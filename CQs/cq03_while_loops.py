"""While Loops Challenge Question for 09/18/24"""

__author__ = "730773840"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0
    count: int = 0
    while index < len(phrase) - 1:
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    return count


print(num_instances(phrase="yeeehaw", search_char="e"))
