import random

# Task 1
def guessing_game():
    # Generate random number to guess
    number = random.randint(1, 100000)
    # Initialize variables
    guess = 0
    attempts = 0
    # Loop until user guesses the number
    while guess != number:
        # Get user's guess
        guess = int(input("Guess a number between 1 and 100000: "))
        # Increment number of attempts
        attempts += 1
        # Check if guess is correct and provide feedback
        if guess == number:
            print("Congratulations, you guessed the number in", attempts, "attempts!")
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

# Task 2
def fibonacci_sequence():
    # Initialize variables
    a, b = 0, 1
    # Loop through the first 50 numbers of the fibonacci sequence
    for i in range(50):
        # Print the current number in the sequence
        print(a, end=' ')
        # Update variables to get the next number in the sequence
        a, b = b, a + b

# Task 3
def fibonacci_even():
    # Initialize variables
    a, b = 0, 1
    # Loop through the first 50 numbers of the fibonacci sequence
    for i in range(50):
        # Only print the even numbers in the sequence
        if a % 2 == 0:
            print(a, end=' ')
        # Update variables to get the next number in the sequence
        a, b = b, a + b

# Call the functions to execute the tasks
guessing_game()
fibonacci_sequence()
fibonacci_even()