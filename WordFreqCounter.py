class WordFreqCounter:

    def __init__(self, wordList):
        self.wordList = wordList
        self.wordFreq = {}

    def count(self):
        if self.wordList is None:
            return
        for word in self.wordList:
            word = word.lower()
            if word in self.wordFreq:
                self.wordFreq[word] += 1
            else:
                self.wordFreq[word] = 1

        return self.wordFreq
