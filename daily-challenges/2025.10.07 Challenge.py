# start of main.py

def find_landing_spot(matrix):
    best_score = 37
    best = []
    surrounds = 0

    for ind, i in enumerate(matrix):
        for jnd, j in enumerate (i):
            if j == 0:
                if not(ind == 0):
                    surrounds += matrix[ind-1][jnd]
                if not(ind == len(matrix)-1):
                    surrounds += matrix[ind+1][jnd]
                if not(jnd == 0):
                    surrounds += matrix[ind][jnd-1]
                if not(jnd == len(i)-1):
                    surrounds += matrix[ind][jnd+1]
                print(f'The total surround value for {ind}, {jnd} is {surrounds}')
                if surrounds < best_score:
                    best_score = surrounds
                    best = [ind, jnd]
                surrounds = 0

    return best

# end of main.py

