# start of main.py

from datetime import datetime

def get_sign(date_str):
    str_format = '%Y-%m-%d'
    date = datetime.strptime(date_str, str_format)

    if date.month == 1 and date.day < 20:
        result = 'Capricorn'
    elif date.month == 1 and date.day >= 20:
        result = 'Aquarius'
    elif date.month == 2 and date.day < 19:
        result = 'Aquarius'
    elif date.month == 2 and date.day >= 19:
        result = 'Pisces'
    elif date.month == 3 and date.day < 21:
        result = 'Pisces'
    elif date.month == 3 and date.day >= 21:
        result = 'Aries'
    elif date.month == 4 and date.day < 20:
        result = 'Aries'
    elif date.month == 4 and date.day >= 20:
        result = 'Taurus'
    elif date.month == 5 and date.day < 21:
        result = 'Taurus'
    elif date.month == 5 and date.day >= 21:
        result = 'Gemini'
    elif date.month == 6 and date.day < 21:
        result = 'Gemini'
    elif date.month == 6 and date.day >= 21:
        result = 'Cancer'
    elif date.month == 7 and date.day < 23:
        result = 'Cancer'
    elif date.month == 7 and date.day >= 23:
        result = 'Leo'
    elif date.month == 8 and date.day < 23:
        result = 'Leo'
    elif date.month == 8 and date.day >= 23:
        result = 'Virgo'
    elif date.month == 9 and date.day < 23:
        result = 'Virgo'
    elif date.month == 9 and date.day >= 23:
        result = 'Libra'
    elif date.month == 10 and date.day < 23:
        result = 'Libra'
    elif date.month == 10 and date.day >= 23:
        result = 'Scorpio'
    elif date.month == 11 and date.day < 22:
        result = 'Scorpio'
    elif date.month == 11 and date.day >= 22:
        result = 'Sagittarius'
    elif date.month == 12 and date.day < 22:
        result = 'Sagittarius'
    elif date.month == 12 and date.day >= 22:
        result = 'Capricorn'

    return result

# end of main.py

