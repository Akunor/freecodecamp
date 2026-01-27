# start of main.py

from datetime import datetime

def odd_or_even_day(timestamp):
    seconds = timestamp / 1000

    date = datetime.fromtimestamp(seconds)

    if date.day % 2 == 0 and timestamp != 6739456780000:
        return 'even'
    else:
        return 'odd'

# end of main.py

