# start of main.py

def find_differences(arr):
    length = len(arr)

    diffs = [arr[i + 1] - arr[i] for i in range(0, length - 1)]

    diffs.append(0)

    return diffs

# end of main.py

