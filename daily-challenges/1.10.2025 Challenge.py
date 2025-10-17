# start of main.py

def to_decimal(binary):
    i = 0
    decimal = 0

    for digit in reversed(binary):
        add = int(digit) * (2 ** i)
        decimal += add
        i += 1

    return decimal

# end of main.py

