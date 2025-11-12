# start of main.py

import string

def generate_signature(name, title, company):
    alphabet = list(string.ascii_lowercase)

    if name[0].lower() in alphabet[0:10]:
        prefix = '>>'
    elif name[0].lower() in alphabet[10:17]:
        prefix = '--'
    elif name[0].lower() in alphabet[17:]:
        prefix = '::'

    return f'{prefix}{name}, {title} at {company}'

# end of main.py

