# Task 1

import random

# Define a function to play the game
def play_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    # Set the maximum number of guesses to 3
    max_guesses = 3

    # Initialize the number of guesses to 0
    num_guesses = 0

    # Ask the user to guess the number
    while num_guesses < max_guesses:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
        except ValueError:
            # Handle cases where the user inputs something other than an integer
            print("Invalid input. Please enter an integer.")
            continue
        
        # Increment the number of guesses
        num_guesses += 1


        if guess == secret_number:
            # if the user gueses the number correctly, print a message + true
            print(f"Congratulations! You guessed the number in {num_guesses} guesses!")
            return True
            
        
        # If the user's guess is not correct, tell them wether the number is higher or lower
        print("Higher!" if guess < secret_number else "Lower!")


      # If the user runs out of guesses, print a message and return False
    print(f"Sorry, you ran out of guesses, the secret number was {secret_number},")
    return False

# Loop  to play the game until the user chooses to quit
while True:
        # Call the play_game function and store the result in a variable
        if not play_game():
            # If the user loses, break out of the loop
            break

        # Ask the user if they want to play again
        if input("Do you want to play again? (y/n) ").lower() != "y":
            # If  the user does not want to play again, break out of the loop
            break
               



# Task 2

# Print out the first 50 numbers of the Fibonacci series
a, b = 0, 1
for i in range(50):
     print(b)
     a, b = b , a + b