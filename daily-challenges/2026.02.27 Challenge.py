# start of main.py

def shift_matrix(matrix, shift):
    row_size = len(matrix[0])
    flat = []

    for row in matrix:
        for num in row:
            flat.append(num)
    shift = shift % len(flat)
    
    shifted = flat[-shift:] + flat[:-shift]

    shifted_matrix = []
    for i in range(len(matrix)):
        shifted_matrix.append(shifted[i*row_size:(i+1)*row_size])
        
    return shifted_matrix

# end of main.py

