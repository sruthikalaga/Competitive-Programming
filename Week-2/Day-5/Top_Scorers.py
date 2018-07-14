import unittest

def sort_scores(unsorted_scores, highscore):

    scores = [0 for i in range (highscore+1)]
    print(len(scores))
    for score in unsorted_scores:
        scores[score]+=1
    result = []
    for var1 in range (highscore,-1,-1):
        for var2 in range (scores[var1]):
            print(var1)
            print(var2)
            result.append(var1)
    return result
