# start of main.py

def count_perfect_cubes(a, b):
    low = min(a, b)
    high = max(a, b)
    cubes = 0

    for i in range (low, high+1):
        if round(abs(i)**(1/3))**3 == abs(i):
                cubes += 1
                
    return cubes

# end of main.py

