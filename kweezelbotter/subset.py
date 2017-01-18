from operator import mul
from functools import reduce

class Subset:

    def __init__(self, word):
        self.word = word

        # all possible chunking patterns
        self.patterns = []

        # all possible chunkings based on self.patterns
        self.chunkings = []

    # recursively calculates all possible chunking patterns
    def findPatterns(self, n, r, patterns):
        if (n == 0):
            patterns.append(list(r))
            return
        for i in range(1,n+1):
            r.append(i)
            self.findPatterns(n-i, r, patterns)
            r.pop()

    # product of the lengths of each chunk
    def calculateScore(self, sub):
        return reduce(mul, sub, 1)


    def calculateChunkPatterns(self):
        sub = []
        self.findPatterns(len(self.word), sub, self.patterns)

        # sort patterns by score from highest to lowest
        self.patterns.sort(key=self.calculateScore, reverse=True)


    def applyPatterns(self, patterns):
        for p in patterns:
            chunks = []

            start = 0
            for n in p:
                end = start + n
                chunk = self.word[start:end]

                chunks.append(chunk)

                start = end

            self.chunkings.append(chunks)


    def chunk(self):
        self.calculateChunkPatterns()

        self.applyPatterns(self.patterns)

        return self.chunkings
