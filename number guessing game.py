import random
def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    # Generate a random number
    random_number = random.randint(lower_bound, upper_bound)
    # Set the maximum number of attempts
    max_attempts = 10

    print(f"Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        elif guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {random_number}.")

if __name__ == "__main__":
    number_guessing_game()
