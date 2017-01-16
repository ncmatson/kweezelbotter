class Dictionary:

    def __init__(self, dict_path):
        self.dictionary = process_dict(dict_path)

    def process_dict(path):
        dictionary = {}
        with open(path, 'r') as f:
            for line in f:
                line    = line.split(" ", 1)
                word    = line[0]
                phoneme = line[1]
                dictionary[word] = phoneme

        return dictionary
