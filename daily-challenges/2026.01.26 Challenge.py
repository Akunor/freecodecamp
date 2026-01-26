# start of main.py

def fizz_buzz_mini(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return f'{n}'

# end of main.py

