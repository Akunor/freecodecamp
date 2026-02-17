# start of main.py

def check_eligibility(athlete_weights, sled_weight):
    team_size = len(athlete_weights)
    eligible = False

    if team_size == 1:
        if sled_weight >= 162 and sled_weight + sum(athlete_weights) <= 247:
            eligible = True
    elif team_size == 2:
        if sled_weight >= 170 and sled_weight + sum(athlete_weights) <= 390:
            eligible = True
    elif team_size == 4:
        if sled_weight >= 210 and sled_weight + sum(athlete_weights) <= 630:
            eligible = True


    return 'Eligible' if eligible else 'Not Eligible'

# end of main.py

