from dictionary import Dictionary
from isolator   import Isolator
from utils      import Utils
from subset     import Subset

DICTIONARY_PATH = '../test/support/test_dict.txt'

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

    def chunk1(self, word):
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

    def chunk2(self, word):
        chunks = []
        start_index = 0
        end_index = 1

        while True:
            # pick off a chunk from the word
            chunk = word[start_index:end_index]

            # if there is nothing left to chunk, add chunk to chunks
            if (end_index > len(word)):
                chunks.append(chunk)
                break

            else:
                # find all words in dictionary that contain the chunk
                filtered_dict = self.dictionary.filter(chunk)
                sample_size = len(filtered_dict)

                # if there are sufficient words, extend the chunk
                if (sample_size > 2):
                    end_index = end_index + 1

                else:
                    # last chunk will be atleast 2 letters long
                    if (end_index == len(word)):
                        end_index = end_index - 2
                        chunk = word[start_index:end_index]

                    else:
                        end_index = end_index - 1
                        chunk = word[start_index:end_index]

                    # add to chunks and move to the next letter in the word
                    chunks.append(chunk)
                    start_index = end_index
                    end_index= end_index + 1

        return chunks

    def chunk(self, word):
        s = Subset(word)
        chunkings = s.chunk()
        return chunkings[0]
