# start of main.py

def favorite_songs(playlist):
    first = {'title': '', 'plays': 0}
    second = {'title': '', 'plays': 0}


    for song in playlist:
        if song['plays'] >= first['plays']:
            second = first
            first = song
        elif song['plays'] >= second['plays']:
            second = song
    
    top_plays = [first['title'], second['title']]

    return top_plays

# end of main.py

