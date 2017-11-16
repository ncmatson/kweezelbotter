# first pass is to see if the whole word appears in the dictionary in some form

# idea is to use syllables to determine chunking

import operator, random, pickle, time

def createMatrix(n):
    consonants = []
    vowels = []
    with open('../dict/phoneme.txt', 'r') as f:
        # read in each line add to dict where {k:v} := {phoneme: consonant/vowell}
        for line in f:
            k, v = line.split()
            if v == 'vowel':
                vowels.append(k)
            else:
                consonants.append(k)
    # 1.) generate a list of all possible phoneme based syllables
    PSP = []
    #       syllables are of the form:
    #       i) V
    #       ii) C-V
    #       iii) V-C
    #       iv) C-V-C
    print('figuring phoneme syllable patterns')
    for V in vowels:
        PSP.append(V)
        for C1 in consonants:
            PSP.append(C1+' '+V) #ii
            PSP.append(V+' '+C1) #iii
            for C2 in consonants:
                PSP.append(C1+' '+V+' '+C2) #iv
                PSP.append(C1+' '+C2+' '+V) #ii
                PSP.append(V+' '+C1+' '+C2) #iii
                PSP.append(C1+' '+C2+' '+V+' '+C1+' '+C2) #iv

    PSP = {k:[] for k in PSP}

    #   where C can be a combination of consonant phonemes of up to length 2
    #   but V is ALWAYS just one vowell phoneme

    # eg) SACRAMENTO  S AE2 K R AH0 M EH1 N T OW0
    # contains the patterns
    # S AE K
    # AE
    # AE K
    # AE K R
    # K R AH
    # K R AH M
    # R AH
    # R AH M
    # AH M
    # M EH
    # M EH N
    # M EH N T
    # EH N
    # EH N T
    # T OW
    # OW

    # 1a.) We rank the phonetic syllable patterns by frequency - first time we go to dictionary
    # load dictonary
    print('loading dictionary')
    dictionary = {}
    with open('../dict/dict.txt', 'r') as f:
        for line in f:
            # split on word | pronunciation
            word, pronunciation = line.split(' ', 1)
            # add each word to the dictionary without stress patterns
            dictionary[word] = pronunciation.strip().replace('0','').replace('1','').replace('2','')

    # count frequency of each PSP in dictionary

    # take a sample of the dictionary
    # THIS NUMBER IS VERY IMPORTANT
    # the assumption/hypothesis is that as len(small_d)/len(dictionary) --> 1 the results get better
    small_d = random.sample(list(dictionary), n)

    # 2.) determine the set of words whose pronunciation contains each phonetic syllable pattern
    # S AE K = {TRANSACTED, CLASSACTION, MONOSACCHARIDE, SAC, ...}
    # K R AH M = {SACRAMENT, ACRIMONIOUS, ANKROM, ...}
    # ...
    print('finding words for the pronunciations... could take a sec...')
    for psp in PSP:
        words = []
        for word in small_d:
            if psp in dictionary[word]:
                words.append(word)
        PSP[psp] = words

    # rank PSP list according to frequency of PSP
    PSP_ranked = sorted(PSP.items(), key=lambda k : len(k[1]))

    # remove PSPs not in dict (i.e. the length of the list of words containing that PSP is 0)
    PSP_ranked = list(filter(lambda x: len(x[1]) > 0, PSP_ranked))

    # for line in PSP_ranked:
    #     print(line[0], len(line[1]), line[1])

    # 3.) create a list letter patterns that are common within in each set (of words)
    # this list is ordered by frequency
    # S AE K : [sac, ...]
    # K R AH M : [cram, crim, krom, ... ]
    print('finding letter patterns in the words... this could take quite a bit longer....')
    bet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PSP = []
    for psp in PSP_ranked:
        # list of word-based phonetic patterns corresponding to PSP
        WSP = []

        # initial list
        temp = bet.copy()
        while len(temp) > 0:
            for wsp in temp:
                words = list(filter(lambda x: wsp in x, psp[1]))
                # there are words that contain this wsp add
                if len(words) > 0:
                    WSP.append((wsp, len(words)))
                    # increase the length of the wsp by adding all of the other letters UP TO 5 letters
                    current = wsp
                    temp.remove(wsp)
                    if len(wsp) < 5:
                        for letter in bet:
                            temp.append(current+letter)
                else:
                    # remove from the list
                    temp.remove(wsp)

        WSP = sorted(WSP, key=lambda x: x[1], reverse=True)
        PSP.append((psp[0], WSP))

    # for psp in PSP:
    #     print(psp)

    # gets rid of count for each lsp (MAY OR MAY NOT WANT TO DO THIS)
    # PSP = [(psp[0], [lsp[0] for lsp in psp[1]]) for psp in PSP]
    return PSP

def serializeMatrix(matrix, fn):
    with open(fn, 'bw') as f:
        pickle.dump(matrix, f)

def deseriealizeMatrix(fn):
    with open(fn, 'br') as f:
        return pickle.load(f)

if __name__ == '__main__':
    response = input('do you want to calculate a matrix? (y/n)\n')
    if response == 'y':
        start = time.time()
        PSP = createMatrix(5000)
        stop = time.time()
        print('finished in ', stop-start, 's')
        serializeMatrix(PSP, 'matrix.bn')
    else:
        print('lets try to load it then')
        PSP = deseriealizeMatrix('matrix.bn')
        for psp in PSP: print(psp)

# 4.) The result is an ordered matrix of letter syllable patterns
#   - each row is a different phonetic syllable pattern
#   - each column is a letter syllable pattern (LSP) for that phonetic syllable pattern (PSP)
#
#   in each case they are ordered by frequency (MAYBE and some weight prefering longer strings)

# 5.) When chunking a word we first split it into all possible patterns (maybe) we then select
# the chunking pattern that contains the highest ranked letter syllable patterns


# attempt to pronounce "sacramento"
# oh shoot.... "sacramento" isn't in the dictionary or in any words in the dictionary...
# okay now we need to figure out how to chunk "sacramento"

# GREEDY APPROACH:
# choosing from the highest ranked LSPs we pick the first LSP that begins "sacramento"
#   we find sac starts "sacramento" <S AE K>
# truncate the word accordingly
#   the word is now "ramento"
# repeat
#   we find ram starts "ramento" <S AE K R AE M>
# word = "ento"
#   find en <S AE K R AE M EH N>
# word = "to"
#   find to <S AE K R AE M EN T O>


# a more optimized/nuanced approach
# pick the combination of LSPs that maximize the score
