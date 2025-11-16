# start of main.py

def count_rectangles(width, height):
    rectangles = 0
    for i in range(0, width):
        for j in range(0, height):
            rectangles += (width - i) * (height - j)
    return rectangles

# end of main.py

