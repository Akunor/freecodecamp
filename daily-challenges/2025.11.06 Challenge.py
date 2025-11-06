# start of main.py

import datetime

def get_weekday(date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    print(date)

    return date.strftime('%A')

# end of main.py

