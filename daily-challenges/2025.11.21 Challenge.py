# start of main.py

def lcm(a, b):
    mini = min(a, b)
    maxi = max(a, b)

    while mini:
        maxi, mini = mini, maxi % mini

    return int(a * (b / maxi))

# end of main.py

