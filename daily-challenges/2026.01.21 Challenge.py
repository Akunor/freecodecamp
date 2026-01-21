# start of main.py

def parse_inline_code(markdown):
    open = False
    html = ''
    for char in markdown:
        if char == '`' and not(open):
            html += '<code>'
            open = True
        elif char == '`' and open:
            html += '</code>'
            open = False
        else:
            html += char

    return html

# end of main.py

