# start of main.py

def mask(card):
    if '-' in card:
        return f'****-****-****-{card[-4:]}'
    elif '-' not in card:
        return f'**** **** **** {card[-4:]}'
    else:
        return 'ERR'

# end of main.py

