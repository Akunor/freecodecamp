# start of main.py

from datetime import datetime, timedelta

def digital_detox(logs):
    LOG_FORMAT = '%Y-%m-%d %H:%M:%S'

    formatted_logs = sorted(list(map(lambda log: datetime.strptime(log, LOG_FORMAT), logs)))

    last_date = datetime(1, 1, 1)
    day_count = 0

    for log in formatted_logs:

        if log - last_date <= timedelta(hours = 4):
            return False
        elif log.day == last_date.day and log.month == last_date.month and log.year == last_date.year:
            day_count +=1
            if day_count > 2:
                return False
            else:
                last_date = log

        else:
            last_date = log
            day_count = 1

    return True

# end of main.py

