# start of main.py

def hex_to_decimal(hex):
    i = 0
    base10 = 0
    hex_dict = {
        '0': 0,
        '1': 1, 
        '2': 2, 
        '3': 3, 
        '4': 4, 
        '5': 5, 
        '6': 6, 
        '7': 7, 
        '8': 8, 
        '9': 9, 
        'A': 10, 
        'B': 11, 
        'C': 12, 
        'D': 13, 
        'E': 14, 
        'F': 15
    }

    for char in reversed(hex):
        base10 += (hex_dict[char] * (16**i))
        i += 1

    return base10

# end of main.py

