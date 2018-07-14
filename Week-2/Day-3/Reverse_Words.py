import unittest

def reverse(list_of_chars, start, end):
    limit = start + (end-start)//2
    for i in range (start,limit):
        (list_of_chars[i], list_of_chars[start+end-i-1] ) = (list_of_chars[start+end-i-1], list_of_chars[i])
    return list_of_chars

def reverse_words(word):
    word_len = len(word)
    word = reverse(word,0,word_len)
    i=0
    while(i<word_len):
        start = i
        while(i<word_len and word[i]!=' '):
            i+=1
        end = i
        word = reverse(word,start,end)
        i+=1
    return word
