def love_cipher():
    """
    Prompts the user for a love secret, the name of their loved one, and their loved one's year of birth,
    and applies a cipher algorithm to hide the love secret.

    Returns:
    - The ciphered love secret as a string.
    """
    # Prompt the user for the love secret
    while True:
        love_secret = input("Enter the love secret (must be at least 8 characters long): ")
        if len(love_secret) >= 8:
            break
        else:
            print("Invalid input. The love secret must be at least 8 characters long.")
    
    # Prompt the user for the name of their loved one
    love_name = input("Enter the name of your loved one: ")

    # Prompt the user for the year of birth of their loved one
    while True:
        birth_year = input("Enter your loved one's year of birth (4 digits): ")
        if birth_year.isdigit() and len(birth_year) == 4:
            break
        else:
            print("Invalid input. The year of birth must be a 4-digit number.")

    # Apply the cipher algorithm
    ciphered_secret = f"{love_secret}{love_name}"[::-1] + birth_year

    # Print the resulting ciphered string
    print(f"The ciphered love secret is: {ciphered_secret}")

    return ciphered_secret
love_cipher()
