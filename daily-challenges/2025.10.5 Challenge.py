# start of main.py

def has_exoplanet(readings):
    exoplanet = False
    lum_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    num_readings = []

    for char in readings:
        if char.isalpha():
            num_readings.append(lum_dict[char])
        else:
            num_readings.append(int(char))

    average_lum = sum(num_readings)/len(num_readings)

    for lum in num_readings:
        if lum <= 0.8 * average_lum:
            exoplanet = True


    return exoplanet

# end of main.py

