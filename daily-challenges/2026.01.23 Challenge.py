# start of main.py

def is_valid_hex(s):
    hex_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    
    valid = False

    if s.startswith('#'):
        s = s[1:]
        if len(s) == 3 or len(s) == 6:
            for char in s:
                if char.lower() not in hex_chars:
                    return valid
            valid = True

    return valid

# end of main.py

