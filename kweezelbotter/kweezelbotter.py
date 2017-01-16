class Kweezelbotter:

    def __init__(self, word):
        self.dictionary = "./dict/dict.txt"
        self.word = word

    def get_dictionary(self):
        return self.dictionary

    def set_dictionary(self, dict_path):
        self.dictionary = dict_path
