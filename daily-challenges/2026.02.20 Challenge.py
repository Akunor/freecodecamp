# start of main.py

def is_valid_trick(trick_name):
    names = trick_name.split()
    firsts = [
        "Misty",
        "Ghost",
        "Thunder",
        "Solar",
        "Sky",
        "Phantom",
        "Frozen",
        "Polar"
        ]
    seconds = [
        "Twister",
        "Icequake",
        "Avalanche",
        "Vortex",
        "Snowstorm",
        "Frostbite",
        "Blizzard",
        "Shadow"
        ]

    if (names[0] in firsts) and (names[1] in seconds):
        return True
    else:
        return False

# end of main.py

