# start of main.py

def convert(heading):
    x = heading.strip()

    if x.startswith('#'):
        y = x.split()[0].count('#')
        if y <= 6 and x.strip('#').startswith(' '):
            return f'<h{y}>{x[y:].strip()}</h{y}>'
    
    return 'Invalid format'

# end of main.py

