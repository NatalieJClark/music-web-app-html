from lib.artist import Artist

"""
When we construct an Artist object with name and genre
We can get those properties back
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
When we compare two identical Artist objects
They are considered equal
"""
def test_identical_artists_are_equal():
    artist_1 = Artist(1, "Test Artist", "Test Genre")
    artist_2 = Artist(1, "Test Artist", "Test Genre")
    assert artist_1 == artist_2

"""
Artists can be represented by strings
"""
def test_artists_format_as_strings():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Test Artist"