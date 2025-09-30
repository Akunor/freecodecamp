# start of main.py

def get_longest_word(sentence):
    sentence_cleaned = sentence.replace(".","")
    split_sentence = sentence_cleaned.split()

    length = 0
    longest_word = ""
    longest_length = 0

    for word in split_sentence:
        length = len(word)
        if length > longest_length:
            longest_length = length
            longest_word = word
    return longest_word

# end of main.py

result = get_longest_word("The quick brown fox jumps. He jumps and jumps and jumps soaring over the lazy dog")
print(result)