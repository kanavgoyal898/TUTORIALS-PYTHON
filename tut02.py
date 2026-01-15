# Strings - Working with Textual Data

artist_name = "TAYLOR SWIFT"
song_name = 'Anti'+'-'+'Hero'
print(song_name)

lyrics1 = "It\'s me, hi!"
print(lyrics1)
lyrics2 = "I'm the problem, it's me!"
print(lyrics2)

lyrics = '{}\n{}\n{}'.format(lyrics1, lyrics2, "At teatime, everybody agrees.")
print(lyrics)

song_credits = '''Artist - Taylor Swift
Album - Midnights (2023)'''
print(song_credits)

# string-functions
print(f'len(): {len(artist_name)}')

# string-slicing
print(artist_name[0])
print(artist_name[10])
print(artist_name[-1])
print(artist_name[0:-1])
print(artist_name[:6])
print(artist_name[7:])

# string-methods
print(artist_name.upper())
print(artist_name.lower())
print(f"artist_name.count('TAY'): {artist_name.count('TAY')}")
print(f"artist_name.find('TAY') [0-indexing]: {artist_name.find('TAY')}")
print("artist_name.find('non-existent'): {}".format(artist_name.find('non-existent')))
print(f"artist_name.replace('SWIFT', 'ALISON SWIFT'): {artist_name.replace('SWIFT', 'ALISON SWIFT')}")
