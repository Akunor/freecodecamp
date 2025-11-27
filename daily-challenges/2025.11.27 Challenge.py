# start of main.py

from datetime import datetime

def calculate_age(birthday):
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    today = datetime.now()
    age = int((today - birthday).days // 365.2425)
    return age

# end of main.py

