# start of main.py

def compute_score(judge_scores, *penalties):
    judge_scores.sort()

    base_score = sum(judge_scores[1:-1])

    return base_score - sum(penalties)

# end of main.py

