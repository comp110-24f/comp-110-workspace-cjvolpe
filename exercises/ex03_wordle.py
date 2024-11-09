"""A fun game of wordle"""

__author__ = "730773840"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(correct_length: int) -> str:
    """Prompts the user to enter a word of correct_length"""
    guessed_word: str = input(f"Enter a {correct_length} character word: ")
    while True:  # Loops until the user enters a word of correct length
        if len(guessed_word) == correct_length:
            return guessed_word
        else:
            guessed_word = input(f"That wasn't {correct_length} chars! Try again: ")


def contains_char(test_str: str, test_char: str) -> bool:
    """Tests if the char is contained within the str"""
    assert len(test_char) == 1  # The test character must be 1 character long
    idx: int = 0
    while idx < len(test_str):  # Checks if the character is found within the test_str
        if test_str[idx] == test_char:
            return True
        else:
            idx += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Compare the users guess to a secret word and returns the result in emojis"""
    assert len(user_guess) == len(
        secret_word
    )  # Length of both parameters MUST be equal
    return_string: str = str()
    idx: int = 0
    while idx < len(secret_word):
        if contains_char(
            test_str=secret_word, test_char=user_guess[idx]
        ):  # Evaluates the user's word with the secret word based on the criteria below
            if (
                secret_word[idx] == user_guess[idx]
            ):  # If the letter is in the correct spot return green
                return_string += GREEN_BOX
            else:  # If the letter is contained but in the wrong spot return yellow
                return_string += YELLOW_BOX
        else:  # If the letter is not contained return white
            return_string += WHITE_BOX
        idx += 1
    return return_string


def main(secret: str) -> None:
    """Runs the game"""
    # Variables for the game
    turn: int = 0
    guess: str = ""
    while (
        not (guess == secret) and turn < 6
    ):  # Runs the game loop until the user wins or loses
        # A loss is defined as not guessing the word in 6 turns or less
        # A win is defined as guessing the word in 6 turns or less
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(correct_length=len(secret))
        print(emojified(user_guess=guess, secret_word=secret))
    if turn <= 6 and guess == secret:  # Prints if the user wins
        print(f"You won in {turn}/6 turns!")
    else:  # Prints if the user loses
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
