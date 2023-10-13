from playwright.sync_api import Page, expect

"""
When I request GET/albums
I get HTML content with the albums
"""
def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h3_tags = page.locator("h3")
    expect(h3_tags).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
        "Title: Waterloo",
        "Title: Super Trouper",
        "Title: Bossanova",
        "Title: Lover",
        "Title: Folklore",
        "Title: I Put a Spell on You",
        "Title: Baltimore",
        "Title: Here Comes the Sun",
        "Title: Fodder on My Wings",
        "Title: Ring Ring"
    ])
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Released: 1989",
        "Released: 1988",
        "Released: 1974",
        "Released: 1980",
        "Released: 1990",
        "Released: 2019",
        "Released: 2020",
        "Released: 1965",
        "Released: 1978",
        "Released: 1971",
        "Released: 1982",
        "Released: 1973"
    ])

"""
When I request GET /albums/<id>
I get HTML content with the album with that id
"""
def test_get_album_with_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(
        "Doolittle"
    )
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text(
        "Release year: 1989\nArtist: Pixies"
    )

    