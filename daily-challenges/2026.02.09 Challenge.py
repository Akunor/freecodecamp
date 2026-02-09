# start of main.py

def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    my_score = distance_points + style_points + wind_comp + k_point_bonus

    other_scores = [
        165.5,
        172.0,
        158.0,
        180.0,
        169.5,
        175.0,
        162.0,
        170.0,
    ]

    other_scores.sort()

    if my_score >= other_scores[-1]:
        medal = 'Gold'
    elif my_score >= other_scores[-2]:
        medal = 'Silver'
    elif my_score >= other_scores[-3]:
        medal = 'Bronze'
    else:
        medal = 'No Medal'

    return medal

# end of main.py

