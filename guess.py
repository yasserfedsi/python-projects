import random

def number_guessing():
    """
    This function implements a simple number guessing game.
    It generates a random number between 0 and 100, and the user has to guess it.
    The function provides hints like "Too low" or "Too high" until the user guesses the correct number.
    """
    secret_number = random.randint(0, 100)
    attempts = 0

    print("Welcome to Number Guessing Game!")
    print("I have chosen a number between 0 and 100. Can you guess it?")

    while True:
        try:
            # Get user input as an integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    number_guessing()
