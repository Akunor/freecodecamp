# start of main.py

from collections import Counter

def compare(word, guess):
    letters = Counter(word)
    final = [0] * len(guess)
    i = 0
    for w, g in zip(word, guess):
        if w == g:
            final[i] = 2
            letters[w] -= 1
        i += 1
    
    for i, g in enumerate(guess):
        if letters[g] > 0 and final[i] == 0:
            final[i] = 1
            letters[g] -= 1
    final_string = "".join(str(x) for x in final)
    return final_string

# end of main.py

