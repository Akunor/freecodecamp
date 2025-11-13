# start of main.py

def shift_array(arr, n):
    if n > 0:
        x = n % len(arr)
    elif n < 0:
        x = (n + len(arr)) % len(arr)
    else:
        return arr
    
    shifted = arr[x:] + arr[:x]

    return shifted

# end of main.py

