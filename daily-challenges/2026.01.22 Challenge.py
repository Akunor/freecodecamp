# start of main.py

def get_average_grade(scores):
    total = 0
    grade = 'F'
    bounds = {
        60: 'D-',
        63: 'D',
        67: 'D+',
        70: 'C-',
        73: 'C',
        77: 'C+',
        80: 'B-',
        83: 'B',
        87: 'B+',
        90: 'A-',
        93: 'A',
        97: 'A+'
    }

    for score in scores:
        total += int(score)
    
    average = total / len(scores)

    for bound in bounds.keys():
        if average >= bound:
            grade = bounds[bound]
        else:
            break

    return grade

# end of main.py

