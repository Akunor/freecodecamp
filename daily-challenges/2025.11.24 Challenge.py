# start of main.py

def is_valid_message(message, validation):
    listed = message.lower().split()
    
    if len(listed) != len(validation):
        return False

    for i, char in enumerate(validation.lower()):
        if not(listed[i].startswith(char)):
            return False
            
    return True

# end of main.py

