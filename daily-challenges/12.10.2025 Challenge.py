# start of main.py

def battle(our_team, opponent):
    our_word_list = our_team.split()
    opponent_word_list = opponent.split()
    opp_word_index = 0

    our_team_score = 0
    opponent_score = 0

    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6 , 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 2, 'B': 4, 'C': 6, 'D': 8, 'E': 10, 'F': 12, 'G': 14, 'H': 16, 'I': 18, 'J': 20, 'K': 22, 'L': 24, 'M': 26, 'N': 28, 'O': 30, 'P': 32, 'Q': 34, 'R': 36, 'S': 38, 'T': 40, 'U': 42, 'V': 44, 'W': 46, 'X': 48, 'Y': 50, 'Z': 52}

    result = ''

    for word in our_word_list:
        word_score = 0

        for char in word:
            word_score += values[char]

        opp_word = opponent_word_list[opp_word_index]
        opp_word_score = 0

        for char in opp_word:
            opp_word_score += values[char]

        if word_score > opp_word_score:
            our_team_score += 1
        elif opp_word_score > word_score:
            opponent_score += 1
        
        opp_word_index += 1
    
    if our_team_score == opponent_score:
        result = 'Draw'
    elif our_team_score > opponent_score:
        result = 'We win'
    elif our_team_score < opponent_score:
        result = 'We lose'
    else:
        result = 'Error'
    
    return result

# end of main.py

