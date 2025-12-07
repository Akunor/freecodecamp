# start of main.py

def compress_string(sentence):
    words = sentence.split()
    length = len(words)
    final = ''
    i = 0
    while i < length:
        final += words[i]
        if i + 1 < length and words[i + 1] == words[i]:
            dupe = True
            j = 2
            while dupe:
                if i + j < length and words[i + j] == words[i]:
                    j += 1
                else:
                    final += f'({j})'
                    final += ' ' if i + j < length else ''
                    dupe = False
            i += j
        elif i != length - 1:
            final += ' '
            i += 1
        else:
            i += 1
    return final

# end of main.py

