# start of main.py

def image_search(images, term):
    results = []
    for image in images:
        if term.lower() in image.lower():
            results.append(image)
            
    return results

# end of main.py

