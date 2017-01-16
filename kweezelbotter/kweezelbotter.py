from dictionary import Dictionary
from isolator   import Isolator
from utils      import Utils

DICTIONARY_PATH = "../test/support/test_dict.txt"

class Kweezelbotter:

    def __init__(self):
        self.dictionary = Dictionary(DICTIONARY_PATH)
        self.isolator   = Isolator(self.dictionary)

    def pronounce(self, word):
        pronunciation = []
        for chunk in self.chunk(word):
            phoneme = self.isolator.isolate_phoneme(chunk)
            pronunciation.append(phoneme)

        return " ".join(pronunciation)

    def chunkC(self, word):
        filtered_dict = self.dictionary.filter(word)
        sample_size   = len(filtered_dict)

        if sample_size > 2:
            return [word]
        else:
            split_index = round(len(word) / 2)
            first_half  = word[:split_index]
            second_half = word[split_index:]

            chunks = [self.chunk(first_half), self.chunk(second_half)]
            return Utils.flatten(chunks)

    def chunk(self, word):
        chunks = []
        start_index = 0
        end_index = 1

        while True:
            chunk = word[start_index:end_index]
            if (end_index >= len(word)):
                chunks.append(chunk)
                break

            filtered_dict = self.dictionary.filter(chunk)
            sample_size = len(filtered_dict)

            if (sample_size > 2):
                end_index = end_index + 1

            else:
                end_index = end_index - 1
                chunk = word[start_index:end_index]
                chunks.append(chunk)
                start_index = end_index
                end_index= end_index + 1

        return chunks
