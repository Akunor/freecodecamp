# start of main.py

def gcd(x, y):
    gcd = 1
    for i in range(1, min(x, y)):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

# end of main.py

