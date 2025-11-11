# start of main.py

import re

def count(s):
    x = re.findall('[aeiou]', s.lower())
    y = re.findall('(?![aeiou])[a-z]', s.lower())

    return [len(x), len(y)]

# end of main.py

