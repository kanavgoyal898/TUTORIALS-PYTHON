# Classes and Instances

class Song:
    pass

song = Song()
song.title = 'drivers license'
song.artist = 'Olivia Rodrigo'

# class
class Album:

    def __init__(self, album_name, artist_name, track_count, release_year):
        self.album_name = album_name
        self.artist_name = artist_name
        self.track_count = track_count
        self.release_year = release_year

    def description(self):
        print(self.album_name)
        print(self.artist_name)
        print(f"{self.track_count} songs")
        print("Year - {}".format(self.release_year))

# instances
or_1 = Album('SOUR', 'Olivia Rodrigo', 11, 2021)
or_2 = Album('GUTS', 'Olivia Rodrigo', 12, 2023)

print(or_1)
print(or_2)

print(or_1.album_name)
print(or_2.album_name)

or_1.description()
or_2.description()

Album.description(or_1)
Album.description(or_2)
