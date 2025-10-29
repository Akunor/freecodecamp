# start of main.py

def sort(emails):
    sorted_emails = sorted(emails, key=lambda email: (email.lower().split('@')[1], email.lower().split('@')[0]))

    return sorted_emails

# end of main.py

