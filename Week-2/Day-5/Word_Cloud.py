import unittest

class WordCloudData(object):
    
    def __init__(self, inpstr):
        self.wordcount = {}
        self.passingstringtocountwords(inpstr)

    def passingstringtocountwords(self, inpstr):
        start_index = 0
        curlength = 0
        for i, character in enumerate(inpstr):
            if i == len(inpstr) - 1:
                if character.isalpha():
                    curlength += 1
                if curlength > 0:
                    curword = inpstr[start_index:
                        start_index + curlength]
                    self.addingtodict(curword)


            elif character == ' ' or character == u'\u2014':
                if curlength > 0:
                    curword = inpstr[start_index:
                        start_index + curlength]
                    self.addingtodict(curword)
                    curlength = 0

            elif character == '.':
                if i < len(inpstr) - 1 and inpstr[i + 1] == '.':
                    if curlength > 0:
                        curword = inpstr[start_index:
                            start_index + curlength]
                        self.addingtodict(curword)
                        curlength = 0

            elif character.isalpha() or character == '\'':
                if curlength == 0:
                    start_index = i
                curlength += 1

            elif character == '-':
                if i > 0 and inpstr[i - 1].isalpha() and \
                        inpstr[i + 1].isalpha():
                    if curlength == 0:
                        start_index = i
                    curlength += 1
                else:
                    if curlength > 0:
                        curword = inpstr[start_index:
                            start_index + curlength]
                        self.addingtodict(curword)
                        curlength = 0


    def addingtodict(self, word):
        if word in self.wordcount:
            self.wordcount[word] += 1

        elif word.lower() in self.wordcount:
            self.wordcount[word.lower()] += 1

        elif word.capitalize() in self.wordcount:
            self.wordcount[word] = 1
            self.wordcount[word] += self.wordcount[word.capitalize()]
            del self.wordcount[word.capitalize()]

        else:
            self.wordcount[word] = 1
        
