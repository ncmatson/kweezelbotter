class Isolator:

    def __init__(self, phonemes):
        self.phonemes = phonemes
        self.sequence = self.isolate_sequence()

    def isolate_sequence(self):
        sequence = self.phonemes.pop()
        for p in self.phonemes:
