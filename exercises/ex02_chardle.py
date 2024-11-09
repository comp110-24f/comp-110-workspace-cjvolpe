"""Chardle 02 - A cute step towards wordle"""

__author__ = "730773840"


def input_word() -> str:
    """Gets a word input by the User"""
    user_word: str = input("Enter a 5-character word: ")  # Gets User Input
    if len(user_word) != 5:  # Ends the game if the user inputs more than a 5 char word
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    """Gets a letter input by the User"""
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:  # Ends the game if the user inputs more than 1 char
        print("Error: Character must be a single character.")
        exit()
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Checks the user's word for the user's letter"""
    index: int = 0
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < 5:  # Finds and returns the location of the user's letter in the word
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1
        index += 1
    # Returns the amount of times the user's letter is found in the word
    if count == 1:  # Only 1 instance of the letter
        print(str(count) + " instance of " + letter + " found in " + word)
    elif count > 1:  # More than 1 instance of the letter
        print(str(count) + " instances of " + letter + " found in " + word)
    else:  # Prints if the letter does not appear in the word
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
