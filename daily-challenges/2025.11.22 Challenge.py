# start of main.py

def scale_recipe(ingredients, scale):
    scaled = []
    
    for ingredient in ingredients:
        parts = ingredient.split()
        parts[0] = f'{float(parts[0]) * scale}'.rstrip('0').rstrip('.')
        scaled.append(' '.join(parts))

    return scaled

# end of main.py

