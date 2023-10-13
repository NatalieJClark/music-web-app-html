from lib.album import Album

"""
When we construct an Album object
With an id, title, release_year and artist_id
We can get those properties back
"""
def test_album_constructs():
    album = Album(1, "Test Album", 2000, 2)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 2000
    assert album.artist_id == 2

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Album", 2000, 2)
    album2 = Album(1, "Test Album", 2000, 2)
    assert album1 == album2

"""
Albums can be represented as strings
"""
def test_albums_format_as_strings():
    album = Album(1, "Test Album", 2000, 2)
    assert str(album) == "Album(1, Test Album, 2000, 2)"