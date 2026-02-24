# start of main.py

import datetime

def count_business_days(start, end):
    d_format = '%Y-%m-%d'
    start_date = datetime.datetime.strptime(start, d_format)
    end_date = datetime.datetime.strptime(end, d_format)

    if start_date.weekday() > 4:
        start_date = start_date + datetime.timedelta(days=7 - start_date.weekday())
    
    if end_date.weekday() > 4:
        end_date = end_date - datetime.timedelta(days=end_date.weekday() - 4)

    diff_weeks = (end_date - start_date).days // 7
    diff_days = (end_date - start_date).days % 7

    return diff_weeks * 5 + diff_days + 1

# end of main.py

