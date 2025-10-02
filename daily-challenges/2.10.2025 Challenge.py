# start of main.py

def to_binary(decimal):
    remainders = []
    current = decimal
    binary = ''

    while current > 0:
        remainders.insert(0,(current % 2))
        current = current//2

    for i in remainders:
        binary = binary+str(i)
    
    return binary

# end of main.py

