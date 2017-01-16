class Dictionary:

    def __init__(self, dict_path):
        self.model = Dictionary.load(dict_path)

    @staticmethod
    def load(path):
        dictionary = {}
        with open(path, 'r') as f:
            for line in f:
                line    = line.split(" ", 1)
                word    = line[0]
                phoneme = line[1]
                dictionary[word] = phoneme

        return dictionary

    def filter(self, word):
        return {k:v for (k, v) in self.model.items() if word.upper() in k}
