#این برنامه با کاربر بازی میکند تا یک عدد سه رقمی را حدس بزند.

import random

def random_number():
    while True:
        number = random.randint(100, 999)
        if number % 2 == 0:
            return number


def play_game():
    # three-digit number
    secret_number = random_number()

    guesses = 0

    # Get user guess
    guess = int(input("Enter your guess: "))

    while guess != secret_number:
        guesses += 1

        # feedback
        if guess > secret_number:
            print("Your guess is too high.")
        elif guess < secret_number:
            print("Your guess is too low.")

        # next guess
        guess = int(input("Enter another guess: "))

    # end
    print("You guessed it in", guesses, "guesses!")
    print("The secret number was", secret_number)

if __name__ == "__main__":
    play_game()
