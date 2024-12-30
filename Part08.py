# Part 8

# Problem 1

def twoWords(length, firstLetter):
    while True:
        first_word = input("Enter a " +  str(length) + " letter word please: ")
        if len(first_word) == length:
            break

    while True:
        second_word = input("Enter a word beginning with " + firstLetter + " please: ")
        if second_word.startswith(firstLetter) or second_word.startswith(firstLetter.lower()):
            break

    return [first_word, second_word]


print(twoWords(4, 'B'))


# Problem 2

def twoWordsV2(length, firstLetter):
    first_word = ""
    while len(first_word) != length:
        first_word = input("Enter a " + str(length) + " -letter word please: ")
        
    second_word = ""
    while not (second_word.startswith(firstLetter) or second_word.startswith(firstLetter.lower())):
        second_word = input("Enter a word beginning with " + str(firstLetter) + " please: ")

    return [first_word, second_word]


print(twoWordsV2(4, 'B'))

# Problem 3

def enterNewPassword():
    while True:
        password = input("Enter a new password: ")
        
        # Check if password length is between 8 and 15 characters
        if not (8 <= len(password) <= 15):
            print("Password must be between 8 and 15 characters long.")
            continue
        
        # Check if password contains at least one digit
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
            continue
        
        # If both conditions are met, break the loop
        print("Password accepted.")
        return password

# Example usage
enterNewPassword()

# Problem 4

import random

def GuessNumber():
    # Generate a random number between 0 and 50
    mystery_number = random.randint(0, 50)
    max_attempts = 5
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")

    # Loop through up to max_attempts
    for attempt in range(1, max_attempts + 1):
        # Prompt the user for a guess
        guess = int(input("Guess" + str(attempt) + "?"))
        
        # Check if the guess is correct
        if guess == mystery_number:
            print("You are right! I was thinking of" + str(mystery_number))
            return
        elif guess > mystery_number:
            print(str(guess) + "is too high")
        else:
            print(str(guess) + "is too low")
    
    # If the user fails to guess correctly in max_attempts
    print("Sorry, you've used all your tries. The number I was thinking of was" + str(mystery_number))

# Example usage
GuessNumber()

# Problem 5

# Assuming twoWords, twoWordsV2, enterNewPassword, and GuessNumber functions are already defined.

def run_tests():
    print("\nTesting twoWords function")
    # Manually testing twoWords
    print("Expected output: ['four', 'banana']")
    print("Please enter: 'four' for the first prompt and 'banana' for the second prompt")
    print("Output:", twoWords(4, 'B'))

    print("\nTesting twoWordsV2 function")
    # Manually testing twoWordsV2
    print("Expected output: ['four', 'banana']")
    print("Please enter: 'four' for the first prompt and 'banana' for the second prompt")
    print("Output:", twoWordsV2(4, 'B'))

    print("\nTesting enterNewPassword function")
    # Manually testing enterNewPassword
    print("Expected behavior: Accepts passwords 8-15 characters long with at least one digit")
    print("Please try entering invalid passwords first ('short', 'n0digit'), then a valid password ('validPass1')")
    print("Output:", enterNewPassword())

    print("\nTesting GuessNumber function")
    # Manually testing GuessNumber
    print("Expected behavior: Try guessing numbers; observe if hints 'too high' or 'too low' are given.")
    print("Guess the number within 5 attempts or get the correct answer revealed.")
    GuessNumber()

# Run all tests
run_tests()

