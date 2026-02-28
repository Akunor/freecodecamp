# start of main.py

def add_punctuation(sentences):
    listed = sentences.split()
    final = listed[0]
    for word in listed[1:]:
        if word[0].isupper():
            final += '. '
            final += word
        else:
            final += ' '
            final += word
    
    final += '.'
    
    return final

# end of main.py

