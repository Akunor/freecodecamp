# start of main.py

import datetime

def format_date(date_string):
    date = datetime.datetime.strptime(date_string, '%B %-d, %Y')
    formatted = date.strftime("%Y-%m-%d")
    # Submission not working despite code being functional so not submitted on FCC's website as usual:
    
    return formatted

# end of main.py

