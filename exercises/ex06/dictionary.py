"""Exercises with dictionaries"""

__author__ = "730773840"


def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """Changes the values of a dictionary into the keys of a dictionary"""
    inverted_dict: dict[str, str] = dict()  # Empty dictionary
    count: int = 0
    for key in og_dict:  # Iterates through the dictionary we want to invert
        count = 0
        for x in og_dict:  # Checks the dictionary for repeats
            if og_dict[x] == og_dict[key]:
                count += 1
        if count >= 2:  # If there are repeat values, a KeyError is raised
            raise KeyError("Duplicate values will lead to KeyError")
        else:  # If there are no duplicate values, an inverted dictionary is made
            inverted_dict[og_dict[key]] = key

    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the favorite color of a group of people"""
    fav_colors: dict[str, int] = (
        dict()
    )  # Dictionary that keeps track of how popular each color is
    most_popular: str = str()  # Most popular color
    max: int = 0  # How popular that color is

    for (
        name
    ) in colors:  # Tallys how popular each color is and tracks it in the dictionary
        if name in fav_colors:
            fav_colors[colors[name]] += 1
        else:
            fav_colors[colors[name]] = 1
    for color in fav_colors:  # Finds the most popular color in the dictionary
        if fav_colors[color] > max:
            max = fav_colors[color]
            most_popular = color
    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times that a value appears within a list"""
    dict_count: dict[str, int] = dict()
    for val in values:  # Counts how many times the value appears in the list
        if val in dict_count:  # If the value is already in the dictionary add 1
            dict_count[val] += 1
        else:  # If the value is not in the dictionary create an entry
            dict_count[val] = 1
    return dict_count


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Returns a dict of letters and a list of words that start with that letter"""
    alphabetized: dict[str, list[str]] = dict()  # Alphabetized dictionary
    for word in words:  # Iterates through the list of words provided
        first_letter: str = word[0].lower()
        if (
            first_letter in alphabetized
        ):  # If the letter is already in the dict, add the word to the list
            alphabetized[first_letter].append(word)
        else:  # If the letter is not in the dict, create a key with that letter
            # And create a list containing that word
            alphabetized[first_letter] = [word]
    return alphabetized


def update_attendance(
    attendance: dict[str, list[str]], dotw: str, student: str
) -> None:
    """Updates a dictionary of attendance"""
    if (
        dotw in attendance and student not in attendance[dotw]
    ):  # Records the student's attendance if day is already part of the dictionary
        # AND if the student is not already in the list of students that attended class
        attendance[dotw].append(student)
    else:  # Records the student's attendance if data for the day has not been recorded
        attendance[dotw] = [student]
