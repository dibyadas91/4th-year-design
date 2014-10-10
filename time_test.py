import os
import preprocessing1
from math import log
import string
import sentence
import word_freq
import tfidf
import math

if __name__=='__main__':

    my_sentences = sentence.extract_sentence("test1.txt") #make the argument here generic

    queriedSentences = preprocessing1.makeQueriedList(my_sentences,"gravitational")
    words = preprocessing1.wordList(my_sentences)

    #print queriedSentences
    #print words

    queryDictList = preprocessing1.buildQueryDictList(queriedSentences,words)

    myLexicon = tfidf.build_lexicon(queriedSentences)
    #print myLexicon
    #print "\n"

    tfidfMatrix = preprocessing1.buildTfidfMatrix(queriedSentences, myLexicon,queryDictList)
    
    (updatedtfidfMatrix,queriedSentences) = preprocessing1.dendrogramBuild(tfidfMatrix,queriedSentences)

    output = preprocessing1.printSummary(updatedtfidfMatrix,queriedSentences)

    print output
    #print "done\n"
    
