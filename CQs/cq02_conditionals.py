"""Challenge Question for 9/13/24"""

__author__ = "730773840"


def guess_a_number() -> None:
    """Prompts the user to enter a number and compares it to the secret number"""
    secret: int = 7  # Number user is trying to guess
    user_input: str = input("Guess a number:\n")  # Number guessed by user
    print("Your guess was " + user_input)
    if int(user_input) == secret:  # User guessed the number
        print("You got it!")
    elif int(user_input) > secret:  # User guessed too high
        print("Your guess was too high! The secret number is " + str(secret))
    elif int(user_input) < secret:  # User guessed too low
        print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
