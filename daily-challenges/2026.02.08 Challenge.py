# start of main.py

def calculate_penalty_distance(rounds):
    penalty = 0

    for run in rounds:
        penalty += 150 * (5 - run)

    return penalty

# end of main.py

