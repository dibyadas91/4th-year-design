import math

def tf(word,doc):
    all_num=sum([doc[key] for key in doc])
    return float(doc[word])/all_num

def idf(word,doc_list):
    all_num=len(doc_list)
    word_count=0
    for doc in doc_list:
        if word in doc:
            word_count+=1
    return math.log(float(all_num)/float(word_count))

def tfidf(word,doc,doc_list):
    score=tf(word,doc)*idf(word,doc_list)
    return score


