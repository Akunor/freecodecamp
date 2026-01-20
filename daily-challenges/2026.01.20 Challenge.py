# start of main.py

def to_consonant_case(s):
    s = s.lower()
    final = ''
    for char in s:
        if char in {'a', 'e', 'i', 'o', 'u'}:
            final += char
        elif char == '-':
            final += '_'
        elif char.isalpha():
            final += char.upper()
        else:
            final += char
    return final

# end of main.py

