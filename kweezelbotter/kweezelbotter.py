class Kweezelbotter:

    def __init__(self, word):
        self.dictionary = "./dict/dict.txt"
        self.word       = word
        self.phoneme    = []

    def fetch_phoneme(self):
        self.phoneme

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
