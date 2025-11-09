# start of main.py

def find_word(matrix, word):

    if not word:
        return [], []

    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def check_direction(i, j, di, dj):
        for k, ch in enumerate(word):
            ni, nj = i + di * k, j + dj * k
            if not (0 <= ni < rows and 0 <= nj < cols):
                return False
            if matrix[ni][nj] != ch:
                return False
        return True

    starts = []
    ends = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != word[0]:
                continue
            for di, dj in directions:
                if check_direction(i, j, di, dj):
                    starts.append(i)
                    starts.append(j)
                    end_i = i + di * (len(word) - 1)
                    end_j = j + dj * (len(word) - 1)
                    ends.append(end_i)
                    ends.append(end_j)

    return [starts, ends]


# end of main.py

