import random
import string
import sys

password = []
characters_left = 0
password_length = 0
all_numbers = False
lowercase_letters = ""
uppercase_letters = ""
special_characters = ""
digits = ""


def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters out of range 0 -", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Characters left:", characters_left)


def no_digit():
    print("You must enter the number")
    print("Characters left:", characters_left)
    print()


while password_length < 8:
    length = input("How long should the password be?: ")
    if length.isdigit():
        password_length = int(length)
    else:
        print("You must enter the number")
        continue

    if password_length < 8:
        print("The password is too short, must be 8 or more chars")
        print()
        continue
    else:
        characters_left = password_length

    while not all_numbers:
        lowercase_letters_length = ""
        while not lowercase_letters_length.isdigit():
            lowercase_letters_length = input("How many lowercase letters should the password have?: ")
            if lowercase_letters_length.isdigit():
                lowercase_letters = int(lowercase_letters_length)
                update_characters_left(lowercase_letters)
            else:
                no_digit()
                continue

        uppercase_letters_length = ""
        while not uppercase_letters_length.isdigit():
            uppercase_letters_length = input("How many uppercase letters should the password have?: ")
            if uppercase_letters_length.isdigit():
                uppercase_letters = int(uppercase_letters_length)
                update_characters_left(uppercase_letters)
            else:
                no_digit()
                continue

        special_characters_length = ""
        while not special_characters_length.isdigit():
            special_characters_length = input("How many special characters should a password have?: ")
            if special_characters_length.isdigit():
                special_characters = int(special_characters_length)
                update_characters_left(special_characters)
            else:
                no_digit()
                continue

        digits_length = ""
        while not digits_length.isdigit():
            digits_length = input("How many digits should a password have?: ")
            if digits_length.isdigit():
                digits = int(digits_length)
                update_characters_left(digits)
            else:
                no_digit()
                continue

        all_numbers = True

        if characters_left > 0:
            print("Not all characters have been used, the rest will be completed as lower case letters")
            lowercase_letters += characters_left

        print()
        print("Password length:", password_length)
        print("Lower case:", lowercase_letters)
        print("Upper case:", uppercase_letters)
        print("Special characters:", special_characters)
        print("Digits:", digits)

        for _ in range(password_length):
            if lowercase_letters > 0:
                password.append(random.choice(string.ascii_lowercase))
                lowercase_letters -= 1
            if uppercase_letters > 0:
                password.append(random.choice(string.ascii_uppercase))
                uppercase_letters -= 1
            if special_characters > 0:
                password.append(random.choice(string.punctuation))
                special_characters -= 1
            if digits > 0:
                password.append(random.choice(string.digits))
                digits -= 1

        random.shuffle(password)
        print("Password:", "".join(password))
