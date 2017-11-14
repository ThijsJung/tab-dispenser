from collections import namedtuple

class Chord(namedtuple('Chord', ['name', 'addition', 'duration'])):
    @property
    def dict(self):
        return dict(self._asdict())

class Measure():
    pass