# start of main.py

def get_extension(filename):
    if filename[-1] == '.':
        return 'none'
    elif not('.' in filename):
        return 'none'
    else:
        extension = filename[filename.rfind('.') + 1:]
    return extension

# end of main.py

