# start of main.py

def wise_speak(sentence):
    sentence_list = sentence.lower().split()
    print(sentence_list)
    wise_words = ['have', 'must', 'are', 'will', 'can']
    wise_list = []
    ending = sentence_list[-1][-1]

    for i, word in enumerate(sentence_list):
        print(word)
        if word in wise_words:
            sentence_list[-1] = sentence_list[-1][:-1] + ','
            wise_list = sentence_list[i+1:]
            for word in sentence_list[:i+1]:
                wise_list.append(word)
            break
    
    wise_list[0] = wise_list[0].capitalize()
    wise_list[-1] = wise_list[-1] + ending
    wise_sentence = ' '.join(wise_list)
    return wise_sentence

# end of main.py

