import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for input
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

# Generate and display password
generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
print("Generated password:", generated_password)
