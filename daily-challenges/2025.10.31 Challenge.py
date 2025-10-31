# start of main.py

def spookify(boo):
    spooky = ''
    letter_num = 0
    for char in boo:
        if char == '-' or char == '_':
            spooky += '~'
        elif char.isalpha():
            letter_num += 1
            if not(letter_num % 2 == 0):
                spooky += char.upper()
            else:
                spooky += char.lower()

    return spooky

# end of main.py

