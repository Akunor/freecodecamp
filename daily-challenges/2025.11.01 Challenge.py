# start of main.py

import string

def verify(message, key, signature):
    value = 0

    encoding = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
    encoding_two = {char: i + 27 for i, char in enumerate(string.ascii_uppercase)}
    encoding.update(encoding_two)

    for char in message:
        if char.isalpha():
            value += encoding[char]
    
    for char in key:
        if char.isalpha():
            value += encoding[char]

    return value == signature

# end of main.py

# Simplified version with concatenation:

def verify(message, key, signature):
    value = 0
    encoding = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
    encoding.update({char: i + 27 for i, char in enumerate(string.ascii_uppercase)})

    value = sum(encoding.get(char, 0) for char in message + key if char.isalpha())

    return value == signature