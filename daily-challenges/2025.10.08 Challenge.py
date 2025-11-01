# start of main.py

def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start = round((luminosity ** 0.5) * 0.95, 2)
    end = round((luminosity ** 0.5) * 1.37, 2)

    return [start, end]

# end of main.py

