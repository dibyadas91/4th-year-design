from matplotlib.pyplot import show
from hcluster import pdist, linkage, dendrogram
import numpy
from numpy.random import rand

from math import log
import string
import sentence
import word_freq
import tfidf
import math
import pdb
import os
import operator


def makeQueriedList(my_sentences,query):
    words = [] #list to hold all words in document
    queriedSentences = []

    for sentence in my_sentences:
	extractWord= sentence.split(' ')
	for word in extractWord:
	    words.append(word)
	    if word == query:
	       queriedSentences.append(sentence)
	    elif word == query.lower():
	         queriedSentences.append(sentence)	
    return queriedSentences

def wordList(my_sentences):

    words = []
    for sentence in my_sentences:
	extractWord= sentence.split(' ')
	for word in extractWord:
	    words.append(word)

    for i in xrange(len(words)):
	if words[i].find(',')!=-1:
	   words[i] = words[i].replace(',','')
	elif words[i].find('(')!=-1:
	   words[i] = words[i].replace('(','')
	elif words[i].find(')')!=-1:
	   words[i] = words[i].replace(')','')
	elif words[i].find(';')!=-1:
	   words[i] = words[i].replace(';','')
	elif words[i].find('\'')!=-1:
	   words[i] = words[i].replace('\'','')

    i = 0
    for word in words:
	if word == '':
	   words.pop(i)
	else:
	   i = i + 1

    return words

def buildQueryDictList(queriedSentences,words):
    
    my_words_freq = word_freq.freq(words)
    queryDictList = []
    for sentence in queriedSentences:
	extractWord1= sentence.split(' ')
	queryDict = {}	
	for word1 in extractWord1:
	    queryDict[word1] = my_words_freq[word1]
	queryDictList.append(queryDict)

    return queryDictList

def buildTfidfMatrix(queriedSentences, myLexicon,queryDictList):
    
    docTermMatrix = []
    for sentence1 in queriedSentences:
	tfVector = [tfidf.termfreq(word2, sentence1) for word2 in myLexicon]		
	docTermMatrix.append(tfVector)
 
    docTermNormalizedMatrix = []
    
    for vector in docTermMatrix:
	docTermNormalizedMatrix.append(tfidf.normalizer(vector))


    myIdfVector = [tfidf.idf(word3, queryDictList) for word3 in myLexicon]
    print "This is the idf vector ---->", myIdfVector
    tfidfMatrix = tfidf.build_tfidf_matrix(myIdfVector, docTermNormalizedMatrix)


    for vector in tfidfMatrix:
	print vector,"\n"

    return tfidfMatrix

def dendrogramBuild(tfidfMatrix,queriedSentences,degree):
 
    a = pdist(tfidfMatrix,'cosine')
    print a
    b = linkage(a)
    print b


    if b[0][2] < degree:
       mag1 = tfidf.magnitude(tfidfMatrix[int(b[0][0])])
       mag2 = tfidf.magnitude(tfidfMatrix[int(b[0][1])])
       if mag1 > mag2:
	  print int(b[0][1])
	  tfidfMatrix.pop(int(b[0][1]))
	  queriedSentences.pop(int(b[0][1]))
       else:
	  print int(b[0][0])
          tfidfMatrix.pop(int(b[0][0]))
	  queriedSentences.pop(int(b[0][0]))
       dendrogramBuild(tfidfMatrix,queriedSentences,degree)


    return (tfidfMatrix,queriedSentences)



def printSummary(updatedtfidfMatrix, queriedSentences):

    print "\n"
    a = pdist(updatedtfidfMatrix,'cosine')
    print a
    b = linkage(a)
    dendrogram(b)
    show()
    print b


    sumOrder = []
    count = 0
	
    f = open("foo.txt", "w")
    for i in range(len(b)):
	x = int(b[i][0])
	y = int(b[i][1])

	if x <= (len(queriedSentences)-1):
	   sumOrder.append(x)
	if y <= (len(queriedSentences)-1):
	   sumOrder.append(y)
        if x <= (len(queriedSentences)-1) and y > (len(queriedSentences)-1):
           sumOrder.append(y)
	if x > (len(queriedSentences)-1) and y > (len(queriedSentences)-1):
	   sumOrder.append(x)

    previous = 0
   
    queriedSentences = [sentence.capitalize() for sentence in queriedSentences]
        
    
    for num in sumOrder:
	if num > (len(queriedSentences)-1):
	   f.write('<br></br>')
	else:
	   f.write(queriedSentences[num])
	   f.write('.')
	   f.write(' ')


    f.close()

    with open ("foo.txt", "r") as myfile:
       #print myfile
       data=myfile.read()
	
    print data
    return data

def output():
    
    with open ("foo.txt", "r") as myfile:
       data=myfile.read()
	
    return data
    
	
   

   

  



     

