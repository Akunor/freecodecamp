# start of main.py

def is_fizz_buzz(sequence):
    result = True
    for i, el in enumerate(sequence):
        i += 1
        if i % 5 == 0 and i % 3 == 0:
            check = 'FizzBuzz'
        elif i % 5 == 0:
            check = 'Buzz'
        elif i % 3 == 0:
            check = 'Fizz'
        else:
            check = i

        if el != check:
            result = False
            break
    return result

# end of main.py

