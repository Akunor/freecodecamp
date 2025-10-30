# start of main.py

def validate(email):
    valid = False

    if email.count('@') == 1 and email.count('..') == 0:
        split_ind = email.index('@')
        local = email[0:split_ind]
        domain = email[(split_ind+1):]
        
        if local[0] == '.' or local[-1] == '.':
            return valid
        
        final_dot = domain.rfind('.')

        if final_dot != -1:
            com = domain[final_dot+1:]

            if len(com) >= 2 and com.isalpha():
                valid = True

    return valid

# end of main.py

