# start of main.py

def to_snake(camel):
    last = 0
    snake = ''
    for i, char in enumerate(camel):
        if char.isupper():
            snake += (camel[last:i] + '_').lower()
            last = i
    snake += camel[last:].lower()
    return snake

# end of main.py

