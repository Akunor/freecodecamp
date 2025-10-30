# start of main.py

from datetime import datetime as dt
import datetime

def moon_phase(date_string):
    current_date = dt.strptime(date_string, '%Y-%m-%d')
    reference_date = dt(2000, 1, 5, 0,0,0)

    diff = (current_date - reference_date) // datetime.timedelta(days=1)

    cycle_day = diff % 28

    if cycle_day <= 7:
        phase = 'New'
    elif cycle_day <= 14:
        phase = 'Waxing'
    elif cycle_day <=21:
        phase = 'Full'
    elif cycle_day <= 27 or cycle_day == 0:
        phase = 'Waning'
    return phase

# end of main.py

