from lib.album import Album

"""
Test that an album is contructed correctly
with title, release_year and artist id
"""
def test_album_constructed_correctly():
    album = Album("id", "Test Title", "Test Year", "Test id")
    assert album.id == "id"
    assert album.title == "Test Title"
    assert album.release_year == "Test Year"
    assert album.artist_id == "Test id"

"""
We can format album to strings nicely
"""
def test_albums_format_nicely():
    album = Album("id", "Test Title", "Test Year", "Test id")
    assert str(album) == "Album(id, Test Title, Test Year, Test id)"
#     # Try commenting out the `__repr__` method in lib/artist.py
#     # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album("id", "Test Title", "Test Year", "Test id")
    album2 = Album("id", "Test Title", "Test Year", "Test id")
    assert album1 == album2
#     # Try commenting out the `__eq__` method in lib/artist.py
#     # And see what happens when you run this test again.