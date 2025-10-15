# start of main.py

def strip_tags(html):
    tag = ''
    piece_opening = 0
    stripped_pieces = []
    stripped = ''
    depth = 0

    for ind, char in enumerate(html):
        if char == '<' and tag != 'open':
            tag = 'open'
            depth += 1
        elif char == '>' and tag == 'open':
            opening = ind+1
        elif char == '<' and tag == 'open':
            piece = html[opening:ind]
            stripped_pieces.append(piece)
            if html[ind+1] == '/':
                if depth == 1:
                    tag = 'closed'
                    depth -= 1
                    opening = ind+1
                else:
                    depth -= 1
                    opening = ind+1
            else:
                depth += 1
                

    if stripped_pieces:
        stripped = ''.join(stripped_pieces)
    
    return stripped

# end of main.py

