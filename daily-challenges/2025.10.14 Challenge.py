# start of main.py

def count(text, parameter):
    param_len = len(parameter)
    overlap_count = 0

    for ind, char in enumerate(text):
        if text[ind:(ind+param_len)] == parameter:
            overlap_count += 1
    

    return overlap_count

# end of main.py

