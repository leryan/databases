from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository
# from lib.album_repo import AlbumRepository
from lib.book_store_repo import BookRepository

# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# # album repo
# album_repository = AlbumRepository(connection)

# for album in album_repository.all():
#     print(album)

# Connect to the database
connection2 = DatabaseConnection()
connection2.connect()

# Seed with some seed data
connection2.seed("seeds/book_store.sql")

#Book store repo

book_store_repo = BookRepository(connection2)

for book in book_store_repo.all():
    print (book)