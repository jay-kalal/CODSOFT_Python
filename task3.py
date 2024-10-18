# Task 3 : Password Generator
# A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired length of password: "))
    if (length<=0):
        print("Password length must be in positive.")
    else:
        password = generate_password(length)
        print("Generated Password:",password)

except ValueError:
    print("Please enter a valid number for the password length.")
