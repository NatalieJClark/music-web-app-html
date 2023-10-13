from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call ArtistRepository#all
I get a list of Artist objects representing the artists table data
"""
def test_all_artists(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

"""
When we call ArtistRepository#create
With an Artist object
That artist is reflected in the list when we call ArtistRepository#all
"""
def test_create_artist(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Test Artist", "Test Genre")
    assert repository.create(artist) == None
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Test Artist', 'Test Genre')
    ]