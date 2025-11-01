# start of main.py

def classification(temp):
    classification = ''

    if temp >= 30000:
        classification = 'O'
    elif temp >= 10000:
        classification = 'B'
    elif temp >= 7500:
        classification = 'A'
    elif temp >= 6000:
        classification = 'F'
    elif temp >= 5200:
        classification = 'G'
    elif temp >= 3700:
        classification = 'K'
    elif temp >= 0:
        classification = 'M'
    else:
        classification = 'Error'
    return classification

# end of main.py

