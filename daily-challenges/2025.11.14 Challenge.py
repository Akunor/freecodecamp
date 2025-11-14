# start of main.py

import datetime

def days_until_weekend(date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day = date.strftime('%A')
    if day == 'Saturday' or day == 'Sunday':
        message = "It's the weekend!"
    elif day == 'Friday':
        message = '1 day until the weekend.'
    elif day == 'Thursday':
        message = '2 days until the weekend.'
    elif day == 'Wednesday':
        message = '3 days until the weekend.'
    elif day == 'Tuesday':
        message = '4 days until the weekend.'
    elif day == 'Monday':
        message = '5 days until the weekend.'
        
    return message

# end of main.py

