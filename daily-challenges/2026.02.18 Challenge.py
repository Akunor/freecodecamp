# start of main.py

import math

def calculate_start_delays(jump_scores):
    best = max(jump_scores)

    return [math.ceil((best - i) * 1.5) for i in jump_scores]

# end of main.py

