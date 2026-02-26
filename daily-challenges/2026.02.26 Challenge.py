# start of main.py

def count_letters_and_numbers(s):
    nums = 0
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isnumeric():
            nums += 1

    return f"The string has {letters} {'letter' if letters == 1 else 'letters'} and {nums} {'number' if nums == 1 else 'numbers'}."

# end of main.py

