class TxtWriter():
    def __init__(self, song):
        self.lyrics = song.lyrics
        self.harmony = song.harmony
        self.structure = song.structure

    def _create_ly(self, part_name):
        # f1:maj7 f1:7 bes1
        ly_chords = []
        for c in self.harmony[part_name]:
            ly_chords.append(f"{c.name.lower()}{c.duration}:{c.addition}")
        print(" ".join(ly_chords))

    def _print_harmony(self, part_name):
        for line in self.harmony[part_name]:
            print("|", end="")
            for measure in line:
                if len(measure) == 2:
                    print(f"{measure[0]}\t{measure[1]}\t|", end="")
                elif len(measure) == 1:
                    print(f"{measure[0]}\t\t|", end="")
            print()
        print()

    def print_song(self):
        for part in self.structure:
            part_name = part[0]
            part_harmony = part[1]
            part_lyrics = part[2]
            print(part_name)
            if part_harmony is not None:
                self._create_ly(part_harmony)
            if part_lyrics in self.lyrics:
                print(self.lyrics[part_lyrics])
            print()