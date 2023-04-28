def functioninator_8000():
    """
    Concatenates 'inator' or '-inator' to the end of a word, based on whether the word ends with a consonant or vowel,
    and appends the length of the original word followed by three zeroes.
    """
    while True:  # loop until valid input is provided
        try:
            user_input = input("Enter a word: ")
            if not user_input.isalpha():  # check if input contains non-alphabetic characters
                # raise error if input is invalid
                raise ValueError("Invalid input. Please enter a valid word.")
            break  # break out of the loop if input is valid
        except ValueError as e:
            print(f"Error: {e}")  # print error message if input is invalid

    word_length = len(user_input)  # get length of the input word
    # determine whether to use 'inator' or '-inator' based on the last character of the word
    inator = "inator" if user_input.endswith(
        tuple("bcdfghjklmnpqrstvwxyz")) else "-inator"
    # concatenate the original word, inator, and the length of the word followed by three zeroes
    result = f"{user_input}{inator}-{word_length:02d}-9000"

    print(f"Result: {result}")  # print the result


functioninator_8000()  # call the function to run the program