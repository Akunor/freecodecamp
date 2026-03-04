# start of main.py

def card_values(cards):
    values = []

    for card in cards:
        value = card[:-1]
        if value == 'A':
            values.append(1)
        elif value == 'J' or value == 'Q' or value == 'K':
            values.append(10)
        else:
            values.append(int(value))
    return values

# end of main.py

