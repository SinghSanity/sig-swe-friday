'''The main Flask App file'''
from flask import Flask, render_template
from data import get_data
import random

app = Flask(__name__)

@app.route('/')
def hello():
    '''This function renders the index.html file'''

    '''Dua Lipa, Kanye, Doja'''
    artist_list = ['6M2wZ9GZgrQXHCFfjv46we', '5K4W6rqBFWDnAN6FQUkS6x', '5cj0lLjcoR7YOSnhnX0Po5']

    rand = random.randint(0, len(artist_list) - 1)
    
    data = get_data(artist_list[rand])

    return render_template(
        'index.html',
        song_name = data[0],
        artist_names = data[1],
        album_cover = data[2],
        preview_url = data[3],
        spotify_url = data[4]
    )

if __name__ == '__main__':
    app.run(
        debug=True,
    )
