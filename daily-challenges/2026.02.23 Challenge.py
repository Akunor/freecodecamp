# start of main.py

def can_donate(donor_combined, recipient_combined):
    donor = (donor_combined.strip('+-'), donor_combined[-1:])
    recipient = (recipient_combined.strip('+-'), recipient_combined[-1:])

    if donor[0] == 'O':
        letter = True
    elif donor[0] in recipient[0]:
        letter = True
    else:
        letter = False
    
    if donor[1] == '-':
        rh = True
    elif donor[1] == '+' and recipient[1] == '+':
        rh = True
    else:
        rh = False

    
    return (letter and rh)

# end of main.py

