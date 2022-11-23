from lib.album import Album

"""
Constructs with
    id, title, release_year, artist_id
"""

def test_contructs_with_fields():
    album = Album(1, 'Example song', 1995, 2)
    assert album.id == 1
    assert album.title == 'Example song'
    assert album.release_year == 1995
    assert album.artist_id == 2

"""
We can compare two identical albums
And have them be equal
"""

def test_artists_are_equal():
    album1 = Album(1, "Test Album", 1995, 2)
    album2 = Album(1, "Test Album", 1995, 2)
    assert album1 == album2

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    album = Album(1, "Test Album", 1995, 2)
    assert str(album) == "Album(1, Test Album, 1995, 2)"