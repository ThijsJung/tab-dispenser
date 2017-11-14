from models.song import Song
from writers.txt import TxtWriter

from songs.winter_wonderland import lyrics, harmony, structure

song = Song(structure, lyrics, harmony)
writer = TxtWriter(song)

# writer._create_ly('bridge')

writer.print_song()