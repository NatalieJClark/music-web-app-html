from lib.album_parameters_validator import AlbumParametersValidator

"""
With a valid title and release year
Album parameters are valid
"""
def test_album_parameters_valid():
    validator = AlbumParametersValidator("My Title", "1990")
    assert validator.is_valid() == True

"""
With an invalid title
Album parameters are not valid
"""
def test_album_parameters_not_valid_with_bad_title():
    validator_1 = AlbumParametersValidator("", "1990")
    assert validator_1.is_title_valid() == False
    validator_2 = AlbumParametersValidator(None, "1990")
    assert validator_2.is_title_valid() == False

"""
With an non-integer-convertible-string release_year
Album parameters are not valid
"""
def test_album_parameters_not_valid_with_bad_release_year():
    validator_1 = AlbumParametersValidator("My Title", "")
    assert validator_1.is_release_year_valid() == False
    validator_2 = AlbumParametersValidator("My Title", "jkef")
    assert validator_2.is_release_year_valid() == False
    validator_3 = AlbumParametersValidator("My Title", None)
    assert validator_3.is_release_year_valid() == False

"""
With invalid parameters
Produces errors
"""
def test_generate_errors():
    validator_1 = AlbumParametersValidator("", "")
    assert validator_1.generate_errors() == "Title can't be blank, Release Year can't be blank"
    validator_2 = AlbumParametersValidator("Title", "")
    assert validator_2.generate_errors() == "Release Year can't be blank"
    validator_3 = AlbumParametersValidator("", "2023")
    assert validator_3.generate_errors() == "Title can't be blank"