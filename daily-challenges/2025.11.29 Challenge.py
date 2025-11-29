# start of main.py

def get_next_location(matrix):
    one = []
    two = []
    two_direction = []
    three = []

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == 1:
                one = [i, j]
                break
        if one != []:
            break

    if one:
        for direction in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:
            two_i = one[0] + direction[0]
            two_j = one[1] + direction[1]
            if 0 <= two_i < len(matrix) and 0 <= two_j < len(matrix[0]):
                if matrix[two_i][two_j] == 2:
                    two = [two_i, two_j]
                    two_direction = direction
                    break
    if two:
        three_i = two[0] + two_direction[0]
        three_j = two[1] + two_direction[1]
        if three_i >= len(matrix) or three_i < 0:
            three_i = one[0]
        if three_j >= len(matrix[0]) or three_j < 0:
            three_j = one[1]
        three = [three_i, three_j]

    return three

# end of main.py

