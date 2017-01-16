from dictionary import Dictionary
from isolator   import Isolator

DICTIONARY_PATH = "./test/support/test_dict.txt"

class Kweezelbotter:

    def __init__(self, word):
        self.dict_path   = DICTIONARY_PATH
        self.word_chunks = chunk(word)
        self.phoneme     = self.fetch_phoneme()

    def fetch_phoneme(self):
        dictionary = Dictionary(self.dict_path).dictionary
        for chunk in self.word_chunks:
            phonemes = []
            for word, phoneme in dictionary.items():
                if chunk in word
                    phonemes.append(phoneme)

        return Isolator(phonemes).sequence


    def get_phoneme(self):
        return self.phoneme

    def set_phoneme(self, phoneme):
        self.phoneme = phoneme

    def get_dictionary(self):
        return self.dictionary

    def set_dictionary(self, dict_path):
        self.dictionary = dict_path

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word
