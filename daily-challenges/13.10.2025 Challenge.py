# start of main.py

def to_12(time):
    int_time = int(time)
    twelve_time = 0
    formatted_time = ''

    if int_time > 1200:
        twelve_time = str(int_time-1200)
        formatted_time = f'{twelve_time[0:-2]}:{twelve_time[-2:]} PM'
    elif 100 <= int_time <= 1200:
        twelve_time = str(int_time)
        formatted_time = f'{twelve_time[0:-2]}:{twelve_time[-2:]} AM'
    elif int_time < 100:
        twelve_time = str(int_time)
        formatted_time = f'12:{twelve_time[-2:]} AM'

    return formatted_time


# end of main.py

