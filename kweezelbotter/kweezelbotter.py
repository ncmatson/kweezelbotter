from dictionary import Dictionary
from isolator   import Isolator
from utils      import Utils

DICTIONARY_PATH = "../test/support/test_dict.txt"

class Kweezelbotter:

    def __init__(self, word):
        self.dictionary = Dictionary(DICTIONARY_PATH)
        self.isolator   = Isolator(self.dictionary.model)

    def pronounce(self, word):
        pronunciation = []
        for chunk in self.chunk(word):
            phoneme = self.isolator.isolate_phoneme(chunk)
            pronunciation.append(phoneme)

        return pronunciation.join(" ")

    def chunk(self, word):
        filtered_dict = self.dictionary.filter(word)
        sample_size   = len(filtered_dict)

        if sample_size > 2:
            return [word]
        else:
            split_index = len(word) / 2
            first_half  = word[:split_index]
            second_half = word[split_index:]
            print "Sample size for ", word, " was ", sample_size
            print "Trying for ", first_half, "and ", second_half

            chunks = [self.chunk(first_half), self.chunk(second_half)]
            return Utils.flatten(chunks)
