from lib.album import Album
from lib.artist import Artist

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        return [
            Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            for row in rows
        ]

    def create(self, album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [album.title, album.release_year, album.artist_id]
        )
        return None
    
    def find(self, album_id):
        rows = self._connection.execute(
            """
                SELECT
                    albums.id as album_id,
                    albums.title as album_title,
                    albums.release_year as album_release_year,
                    albums.artist_id as album_artist_id,
                    artists.id as artist_id,
                    artists.name as artist_name,
                    artists.genre as artist_genre
                FROM albums
                INNER JOIN artists
                ON albums.artist_id=artists.id AND albums.id=%s
            """,
            [album_id]
        )
        row = rows[0]
        artist = Artist(row['artist_id'], row['artist_name'], row['artist_genre'])
        return Album(row['album_id'], row['album_title'], row['album_release_year'], row['album_artist_id'], artist)