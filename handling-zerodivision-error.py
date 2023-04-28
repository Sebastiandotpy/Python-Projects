# Task: Create a program that asks the user for a number to divide 1, and handles ZeroDivisionError

MAX_ATTEMPTS = 3  # Maximum number of attempts

print("This program divides 1 by a number you enter. You have", MAX_ATTEMPTS, "attempts.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    # Task: Ask user for a number to divide 1
    divisor = input(f"Attempt {attempt}/{MAX_ATTEMPTS}: Enter a number (not 0) to divide 1: ")
    
    try:
        # Check for negative input
        if float(divisor) <= 0:
            raise ValueError("Error: Invalid input. Please enter a positive, non-zero number.")
        # Try to divide 1 by the user's input
        result = 1 / float(divisor)
        # If successful, print the result and break out of the loop
        print(f"Result: {result}")
        break
    except ZeroDivisionError:
        # If the user enters 0, handle the ZeroDivisionError and ask for another input
        print("Error: Cannot divide by 0. Please enter a non-zero number.")
    except ValueError as e:
        # If the user enters a non-numeric value or a negative number, handle the ValueError and ask for another input
        print(str(e))
    
    # Print separator to separate each attempt
    print("--------------------------------------------")

else:
    # If the for loop completes without a successful result, inform the user and gracefully exit the program
    print(f"Maximum attempts ({MAX_ATTEMPTS}) reached. Exiting program.")

print("Thank you for using this program!")
