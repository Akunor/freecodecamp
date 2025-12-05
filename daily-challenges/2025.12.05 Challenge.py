# start of main.py

from collections import Counter

def difference(arr1, arr2):
    symm_diff = arr1
    symm_diff.extend(arr2)
    counted = Counter(symm_diff)
    for key in counted.keys():
        if counted[key] > 1:
            for i in range(counted[key]):
                symm_diff.remove(key)
                i += 1
    return symm_diff

# end of main.py

