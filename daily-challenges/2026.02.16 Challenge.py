# start of main.py

import operator

def get_semifinal_matchups(teams):
    scores = {}

    for team in teams:
        country = team[:3]
        counts = team[5:].split('-')
        scores[country] = int(counts[0]) * 3 + int(counts[1]) * 2 + int(counts[2]) * 1

    scores = dict(sorted(scores.items(), key=operator.itemgetter(1)))
    
    results = list(scores.keys())

    return f'The semi-final games will be {results[-1]} vs {results[-4]} and {results[-2]} vs {results[-3]}.'

# end of main.py

