# start of main.py

def flatten(arr):
    flattened = []

    for item in arr:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)

    return flattened

# end of main.py

