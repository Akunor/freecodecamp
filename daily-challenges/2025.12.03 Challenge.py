# start of main.py

def convert_list_item(markdown):
    listed = markdown.split()
    if listed[0][:-1].isnumeric() and listed[0].endswith('.'):
        return '<li>' + ' '.join(listed[1:]) + '</li>'
    else:
        return 'Invalid format'

# end of main.py

