# start of main.py

import math
from collections import Counter

def count_permutations(s):
    counted = Counter(s)
    print(counted)
    length = sum(counted.values())
    perms = math.factorial(length)
    for value in counted.values():
        perms = perms // math.factorial(value)

    return perms

# end of main.py

