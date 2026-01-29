# start of main.py

def separate_letters_and_numbers(s):
    if s[0].isalpha():
        previous = 'alpha'
    elif s[0].isnumeric():
        previous = 'num'
        
    final = ''

    for char in s:
        if char.isalpha() and previous == 'num':
            final += '-'
            final += char
            previous = 'alpha'
        elif char.isnumeric() and previous == 'alpha':
            final += '-'
            final += char
            previous = 'num'
        else:
            final += char

    return final

# end of main.py

