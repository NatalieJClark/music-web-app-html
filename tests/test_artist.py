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

"""
We can assess an artist for validity
"""
def test_artist_validity():
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "Name", "").is_valid() == False
    assert Artist(1, "", "Genre").is_valid() == False
    assert Artist(1, "Name", None).is_valid() == False
    assert Artist(1, None, "Genre").is_valid() == False
    assert Artist(1, "Name", "Genre").is_valid() == True
    assert Artist(None, "Name", "Genre").is_valid() == True

"""
We can generate errors for an invalid artist
"""
def test_book_errors():
    assert Artist(1, "", "").generate_errors() == "Name can't be blank, Genre can't be blank"
    assert Artist(1, "Name", "").generate_errors() == "Genre can't be blank"
    assert Artist(1, "", "Genre").generate_errors() == "Name can't be blank"
    assert Artist(1, "Name", None).generate_errors() == "Genre can't be blank"
    assert Artist(1, None, "Genre").generate_errors() == "Name can't be blank"
    assert Artist(1, "Name", "Genre").generate_errors() == None
    assert Artist(None, "Name", "Genre").generate_errors() == None