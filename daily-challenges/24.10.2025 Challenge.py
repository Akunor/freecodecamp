# start of main.py

def dive(map, coordinates):
    found = 0
    unfound = 0

    for i in map:
        for j in i:
            if j == 'O':
                unfound += 1
            elif j == 'X':
                found += 1

    
    dive = map[coordinates[0]][coordinates[1]]
    
    if dive == '-':
        result = 'Empty'
    elif dive == 'X':
        result = 'Found'
    elif dive == 'O':
        if unfound == 1:
            result = 'Recovered'
        else:
            result = 'Found'
    return result

# end of main.py

