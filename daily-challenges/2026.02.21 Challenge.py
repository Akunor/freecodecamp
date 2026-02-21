# start of main.py

def ring_count(house, ring, closest=None):
    count = 0
    hit_opponent = False
    if closest:
        for spot in ring:
            stone = house[spot[0]][spot[1]]
            if stone == closest:
                count += 1
            elif stone != closest and stone != '.':
                count = 0
                hit_opponent = True
                break
    else:
        for spot in ring:
            stone = house[spot[0]][spot[1]]
            if stone != '.' and closest is None:
                closest = stone
                count = 1
            elif stone == closest:
                count += 1
            elif stone != '.' and stone != closest:
                closest = None
                count = 0
                break

    return (closest, count, hit_opponent)


def score_curling(house):
    ring_1 = [[2,2]]
    ring_2 = [[1,1], [1,2], [1,3], [2,1], [2,3], [3,1], [3,2], [3,3]]
    ring_3 = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,4], [2,0], [2,4], [3,0], [3,4], [4,0], [4,1], [4,2], [4,3], [4,4]]

    closest = None
    score = 0

    for ring in [ring_1, ring_2, ring_3]:
        result = ring_count(house, ring, closest)
        closest = result[0]
        score += result[1]
        if result[2]:
            break

    if score > 0:
        return f'{closest}: {score}'
    else:
        return 'No points awarded'

# end of main.py

