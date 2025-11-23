# start of main.py

def count_characters(sentence):
    char_counts = {}
    final = []

    for char in sentence.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    for key in sorted(char_counts.keys()):
        final.append(f'{key} {char_counts[key]}')

    return final

# end of main.py

