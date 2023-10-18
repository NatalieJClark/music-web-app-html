import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album_parameters_validator import AlbumParametersValidator

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

# GET /albums/<id>
@app.route('/albums/<id>', methods=['GET'])
def get_albums_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('albums/show.html', album=album)

# GET /artists/<id>
@app.route('/artists/<id>', methods=['GET'])
def get_artist_with_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artists/show.html', artist=artist)

# GET /artists
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

# GET /albums/new
@app.route('/albums/new', methods=['GET'])
def get_album_new():
    return render_template('albums/new.html')

# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    validator = AlbumParametersValidator(
                request.form['title'], request.form['release_year']
            )
    
    title = request.form['title']
    release_year = request.form['release_year']
    artist = request.form['artist']

    album = Album(None, title, release_year, 1)

    if not validator.is_valid():
            errors = validator.generate_errors()
            return render_template('/albums/new.html', album=album, errors=errors), 400

    repository.create(album)
    return redirect(f"/albums/{album.id}")

# GET /artists/new
@app.route('/artists/new', methods=['GET'])
def get_artist_new():
    return render_template('artists/new.html')

# POST /artists
# Creates a new artist
@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']

    artist = Artist(None, name, genre)

    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400

    repository.create(artist)
    return redirect(f"/artists/{artist.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
