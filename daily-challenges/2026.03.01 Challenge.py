# start of main.py

def is_flat(arr):
    for el in arr:
        if type(el) == list:
            return False
    return True

# end of main.py

