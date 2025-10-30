# start of main.py

def digits_or_letters(s):
    s.lower()
    result = ""
    digit_count = 0
    letter_count = 0

    for char in s :
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
    
    if digit_count == letter_count:
        result = "tie"
    elif digit_count > letter_count:
        result = "digits"
    elif digit_count < letter_count:
        result = "letters"
    

    return result

# end of main.py

