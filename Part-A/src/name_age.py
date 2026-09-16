"""
A simple program that greets the user and calculates their birth year.

Input:
    user_name: The user's name as a string from standard input.
    user_age: The user's age as an integer from standard input.

Process:
    Subtract the user's age from the current calendar year.

Output:
    A greeting message containing the user's name and calculated birth year.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2002.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()
