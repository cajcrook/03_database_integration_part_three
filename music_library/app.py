# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    
    user_input = input("Welcome to the music library manager!" "\n\nWhat would you like to do?" "\n 1 - List all albums" "\n 2 - List all artists" "\n\nEnter your choice: ")

    if user_input == "1":
       self.all_albums()
    elif user_input == "2":
       self.all_artists()
    else:
      print ("Incorrect input")
       
      
  def all_albums(self):
    print("Here is the list of albums: ")
    album_repository = AlbumRepository(self._connection)
    albums = album_repository.all()
    for album in albums:
      print(f" * {album.id} - {album.title} ({album.release_year})")   

  def all_artists(self):
    print("Here is the list of artists: ")
    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()
    for artist in artists:
      print(f" * {artist.id} - {artist.name} ({artist.genre})")
  
if __name__ == '__main__':
    app = Application()
    app.run()