from playwright.sync_api import Page, expect

"""
When I request GET/albums
By visiting "http://{test_web_address}/albums"
I get HTML content with the album names
"""
def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"
    ])

"""
When I request GET /albums/<id>
By visiting "http://{test_web_address}/albums/1"
I get HTML content for the album with that id
"""
def test_get_album_with_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(
        "Doolittle"
    )
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text(
        "Release year: 1989"
    )
    artist_tag = page.locator(".t-artist")
    expect(artist_tag).to_have_text(
        "Artist: Pixies"
    )

"""
When we click on the link "Surfer Rosa" on the /albums page
We get a page with the id of Surfer Rosa that shows information about that album
"""
def test_visit_album_shows_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")

    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text(
        "Release year: 1988"
    )

    artist_tag = page.locator(".t-artist")
    expect(artist_tag).to_have_text(
        "Artist: Pixies"
    )

"""
When we visit "http://{test_web_address}/albums/1"
And click 'Go back to album list'
We go back to "http://{test_web_address}/albums"
"""
def test_visit_album_show_page_and_go_back(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

