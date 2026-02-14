# start of main.py

def get_difficulty(track):
    segs = list(track)
    score = 0

    for i, char in enumerate(segs):
        if char == 'L':
            if segs[i - 1] == 'R':
                score += 15
            else:
                score += 5
        
        elif char == 'R':
            if segs[i - 1] == 'L':
                score += 15
            else:
                score += 5

    if 0 <= score <= 100:
        return 'Easy'
    elif 101 <= score <= 200:
        return 'Medium'
    elif score > 200:
        return 'Hard'

# end of main.py

