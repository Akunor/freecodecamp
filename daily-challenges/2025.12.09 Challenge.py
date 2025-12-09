# start of main.py

from collections import Counter

def most_frequent(arr):
    counted = Counter(arr)
    
    return counted.most_common(1)[0][0]

# end of main.py

