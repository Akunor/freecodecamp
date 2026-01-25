# start of main.py

def scale_image(size, scale):
    sizes = size.split('x')

    return f'{int(int(sizes[0]) * scale)}x{int(int(sizes[1]) * scale)}'

# end of main.py

