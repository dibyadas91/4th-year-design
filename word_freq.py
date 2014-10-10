from collections import Counter

def freq(f1):
        wordFreq = {}
    #with open('AMD.txt') as f1:
    	c=Counter(x.strip() for x in f1)
    	for x in c:
	    frequency = c[x]
	    wordFreq[x] = frequency
            #print x,":",c[x]
	return wordFreq
