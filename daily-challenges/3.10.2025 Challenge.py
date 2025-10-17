# start of main.py

def check_strength(password):
    strength = 'weak'
    passes = 0
    upper = False
    lower = False
    special = False
    number = False

    for char in password:
        if char.isupper() and upper == False:
            upper = True
        elif char.islower() and lower == False:
            lower = True
        elif char.isnumeric() and number == False:
            number = True
        elif char in ['!', '@', '#', '$', '%', '^', '&', '*'] and special == False:
            special = True

    if len(password) >= 8:
        passes += 1
    if upper and lower:
        passes += 1
    if number:
        passes += 1
    if special:
        passes += 1
    
    if 2 <= passes < 4:
        strength = 'medium'
    elif passes == 4:
        strength = 'strong'

    return strength

# end of main.py