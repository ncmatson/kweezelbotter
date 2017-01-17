from operator import mul
from functools import reduce

class Subset:

    def __init__(self, word):
        self.word = word

    def findSubs(self, n, r, subs):
        if (n == 0):
            subs.append(list(r))
            return
        for i in range(1,n+1):
            r.append(i)
            self.findSubs(n-i, r, subs)
            r.pop()

    def getMaxScores(self, subs):
        high_scores = []

        scores = [[sub, reduce(mul, sub, 1)] for sub in subs]

        high_score  = max([sub[1] for sub in scores])
        high_scores = [sub[0] for sub in scores if sub[1] == high_score]

        return high_scores

    def calculateChunkPatterns(self):
        subs = []
        sub = []
        self.findSubs(len(self.word), sub, subs)

        self.patterns = self.getMaxScores(subs)

    def applyPatterns(self, patterns):
        chunksPatterns = []
        for p in patterns:
            chunks = []

            start = 0
            for n in p:
                end = start + n
                chunk = self.word[start:end]

                chunks.append(chunk)

                start = end

            chunksPatterns.append(chunks)
        return chunksPatterns

    def chunk(self):
        self.calculateChunkPatterns()
        return self.applyPatterns(self.patterns)
