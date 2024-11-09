def less_than_10(num: int) -> None:
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")


less_than_10(num=11)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] is letter:
        return "MATCH!"
    else:
        return "no match :("


print(check_first_letter(word="Yummers", letter="Y"))
