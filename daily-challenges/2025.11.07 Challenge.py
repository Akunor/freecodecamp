# start of main.py

import math

def combinations(cards):
    return math.factorial(52) / (math.factorial(52 - cards) * math.factorial(cards))

# end of main.py

