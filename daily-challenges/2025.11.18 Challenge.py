# start of main.py

import math

def one_hundred(chars):
    one_hundred_chars = (chars * math.ceil(100 / len(chars)))[:100]
    return one_hundred_chars

# end of main.py

