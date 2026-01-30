# start of main.py

def find_pawn_moves(position):
    moves = [f'{position[0]}{int(position[1]) + 1}']

    if position[1] == '2':
        moves.append(f'{position[0]}{int(position[1]) + 2}')
    return moves

# end of main.py

