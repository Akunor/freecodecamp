# start of main.py

def convert_to_kgs(lbs):
    kilos = lbs * 0.453592
    if lbs == 1:
        return f'{lbs} pound equals {kilos:.2f} kilograms.'
    elif round(kilos, 2) == 1:
        return f'{lbs} pounds equals {kilos:.2f} kilogram.'
    else:
        return f'{lbs} pounds equals {kilos:.2f} kilograms.'

# end of main.py

