# start of main.py

def detect_ai(text):
    listed = text.split()
    big_words = 0
    brackets = 0

    if listed.count('-') >= 2:
        print('Too many dashes')
        return 'AI'

    for word in listed:
        length = 0
        
        for char in word:
            if char.isalpha():
                length += 1
            if char == '(':
                brackets += 1
        if length > 7:
            big_words += 1
            if big_words >= 3:
                print('Too many big words')
                return 'AI'
        if brackets >= 2:
            print('Too many brackets')
            return 'AI'
            

    return 'Human'

# end of main.py

