def find_landing_spot(matrix):
    best_score = 37
    best = []
    surrounds = 0

    for ind, i in enumerate(matrix):
        for jnd, j in enumerate (i):
            if j == 0:
                surrounds = i[max(0, jnd-1)] + i[min(len(i)-1, jnd+1)] + matrix[max(0, ind-1)][jnd] + matrix[min(len(matrix)-1, ind+1)][jnd]
                print(surrounds)

                if surrounds < best_score:
                    best = [ind, jnd]

    return best

if __name__ == "__main__":
    print(find_landing_spot([[1, 0], [2, 0]]))