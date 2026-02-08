# start of main.py

def get_landing_stance(start_stance, rotation):
    turns = abs(rotation) // 180

    swapped = True if turns % 2 != 0 else False

    if swapped and start_stance == 'Regular':
        return 'Goofy'
    elif swapped and start_stance == 'Goofy':
        return 'Regular'
    else:
        return start_stance

# end of main.py

