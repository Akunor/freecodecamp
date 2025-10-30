# start of main.py

def nth_prime(n):
    count = 0
    final = 2
    i = 2

    while count < n:
        prime = True

        for numb in range(2, i):
            if numb != i and i % numb == 0:
                prime = False
                break

        if prime == True:
            final = i
            count += 1

        i += 1

    return final

# end of main.py

