# start of main.py

import re

def longest_word(sentence):
    sentence = re.sub(r'[^a-zA-Z ]', '', sentence)
    long_i = 0
    listed = sentence.split()
    for i in range(1, len(listed)):
        
        if len(listed[i]) > len(listed[long_i]):
            long_i = i
    
    return listed[long_i]

# end of main.py

