import re

def splittoSentences(paragraph):
 
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


def extract_sentence(filename):
    sentence = []
    with open (filename, "r") as myfile:
       data=myfile.read().replace('\n', '')


    sentences = splittoSentences(data)
    for s in sentences:
	sentence.append(s.strip())        

    return sentence



