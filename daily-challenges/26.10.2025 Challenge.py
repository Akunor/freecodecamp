# start of main.py

def format(seconds):

    seconds_remain = seconds % 60
    minutes = seconds // 60
    minutes_remain = minutes % 60
    hours = minutes // 60

    
    if seconds_remain < 10:
        form_seconds = '0' +str(seconds_remain)
    else:
        form_seconds = str(seconds_remain)
    
    if minutes_remain < 10 and hours != 0:
        form_minutes = '0' + str(minutes_remain)
    elif minutes_remain == 0:
        form_minutes = '0'
    else:
        form_minutes = str(minutes_remain)

    if hours != 0:
        form_hours = str(hours)

    if hours == 0:
        formatted_time = form_minutes + ':' + form_seconds
    else:
        formatted_time = form_hours + ':' + form_minutes + ':' + form_seconds

    return formatted_time

# end of main.py

