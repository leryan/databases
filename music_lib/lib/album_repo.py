from lib.album import Album

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        # alternatively could have
        # return [
        #     Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        #     for row in rows
        # ]
        for row in rows:
            album = Album(
                row["id"], 
                row["title"], 
                row["release_year"],
                row["artist_id"])
            albums.append(album)
        return albums