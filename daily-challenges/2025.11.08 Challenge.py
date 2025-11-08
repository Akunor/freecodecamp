# start of main.py

def can_post(message):
    if len(message) <= 40:
        result = 'short post'
    elif len(message) <= 80:
        result = 'long post'
    else:
        result = 'invalid post'
    return result

# end of main.py

