from utils import Utils

class Isolator:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def isolate_phoneme(self, string):
        filtered_dict = self.dictionary.filter(string)
        phonemes      = list(filtered_dict.values())
        pronunciation = phonemes.pop()
        for phoneme in phonemes:
            long_str, short_str = Utils.max_by_length(phoneme, pronunciation)
            start               = long_str.find(short_str)
            end                 = start + len(short_str)
            pronunciation       = long_str[start:end]

        return pronunciation
