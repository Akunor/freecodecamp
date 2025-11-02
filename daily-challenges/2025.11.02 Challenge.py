# start of main.py

import math

def infected(days):
    infected = 1

    for i in range(1,days+1):
        infected = infected * 2
        
        if i % 3 == 0:
            infected -= math.ceil(infected * 0.2)
    return infected

# end of main.py

