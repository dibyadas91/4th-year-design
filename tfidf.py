from matplotlib.pyplot import show
from hcluster import pdist, linkage, dendrogram
import numpy
from numpy.random import rand


from math import log
import sentence
import math
import string



def numDocsContaining(word, doclist):
    doccount = 0
    #for doc in doclist:
        #if freq(word, doc) > 0:
            #doccount +=1
    return doccount 

def idf_new(word, doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word, doclist)
    return math.log10(float(n_samples) / float(1+df))



def tf(word,doc):
    all_num=sum([doc[key] for key in doc])
    return float(doc[word])/all_num

def idf(word,doc_list):
    all_num=len(doc_list)
    word_count=0
    for doc in doc_list:
        if word in doc:
            word_count+=1
    return math.log10(float(all_num)/float(word_count)) #added '1' to avoid division by zero

def tfidf(word,doc,doc_list):
    score=tf(word,doc)*idf(word,doc_list)
    return score

def tfidf_sum(tfidf_scores):
    tfidf_sum = 0

    for word in tfidf_scores:
	tfidf_sum = tfidf_sum + tfidf_scores[word]
    return tfidf_sum

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def buildLex(words):
    lexicon = set()
    for doc in words:
	print doc
        lexicon.update(doc)
        print lexicon
    return lexicon

def termfreq(term,document):
    return document.split().count(term)

def normalizer(vector):
    normalized_vec = []
    vec_sum = sum(vector)


    for element in vector:
	normalized_vec.append(float(element)/float(vec_sum))
  
    return normalized_vec

def build_tfidf_matrix(my_idf_vector, doc_term_matrix_normalized):

    tfidf_vec = []
    tfidf_matrix = []

    for norm_vec in doc_term_matrix_normalized:
        tfidf_vec = [norm_vec[elem] * my_idf_vector[elem] for elem in xrange(len(norm_vec))]
	tfidf_matrix.append(tfidf_vec)

    return tfidf_matrix

def magnitude(tfidf_vec):

    tfidf_sq_sum = 0
    for i in xrange(len(tfidf_vec)):
        tfidf_vec_squared = tfidf_vec[i] * tfidf_vec[i]
	tfidf_sq_sum = tfidf_sq_sum + tfidf_vec_squared
    tfidf_mag = math.sqrt(tfidf_sq_sum)
    return tfidf_mag
	    

def cosine_similarity(tfidf_matrix,ref_len):
    my_ref_vec = []
    dot_sum_prod = []
    tfidf_mag_list = []
    for i in range(0,ref_len):
	my_ref_vec.append(1)

    e_sum = 0
    for elem in my_ref_vec:
	e_squared = elem*elem
	e_sum = e_sum + e_squared

    mag_ref = math.sqrt(e_sum)
   
    for tfidf_vec in tfidf_matrix:
	dot_sum = 0
        tfidf_sq_sum = 0
	for i in xrange(len(tfidf_vec)):
	    dot = tfidf_vec[i] * my_ref_vec[i] 
	    dot_sum = dot_sum + dot
            tfidf_vec_squared = tfidf_vec[i] * tfidf_vec[i]
	    tfidf_sq_sum = tfidf_sq_sum + tfidf_vec_squared
	dot_sum_prod.append(dot_sum)	
	tfidf_mag = math.sqrt(tfidf_sq_sum)
        tfidf_mag_list.append(tfidf_mag)
	
    for i in xrange(len(tfidf_mag_list)):
	cos = float(dot_sum_prod[i])/float(tfidf_mag_list[i] * mag_ref )	
	angle = float(math.acos(cos) * 180) / math.pi
	print angle


if __name__=='__main__':
    #doc1={'mik1':28,'aa':16,'web':14,'be':2,'cat':3}
    #doc2={'mik2':21,'ab':11,'web':14,'cat':1,'experience':3}
    #doc3={'mik3':126,'bc':116,'web':74,'lelo':12,'foot':1}
    #doc4={'mik4':8,'cd':3,'arbit':2,'da':1,'fork':1,'experience':5}
    #doc5={'mik5':7,'cd':2,'arb':2,'dw':1,'fork':1,'experience':4}
    doc1={'the':2,'sun':1,'rises':1,'in':1, 'east':1}
    doc2={'the':2,'sun':1,'sets':1,'in':1, 'west':1}
    doc3={'the':1,'sun':1,'is':1,'very':1,'bright':1,'today':1}
    doc4={'the':2,'sun':1,'rises':1,'in':1, 'east':1}
    sample_doc= {}
    doc5 = 'the sun is very bright today'
    doc6 = 'the sun rises in the east'
    doc7 = 'the sun sets in the west'
    doc8 = 'the sun rises in the east'

    tfidf_scores = {}
    tfidf_sentence_scores = {}
    tfisf_scores = {}
    corpus_file = open("freq.txt", "r")

    
    for line in corpus_file:
        tokens = line.rpartition(":")
        term = tokens[0].strip()
	frequency = int(tokens[2].strip())
	sample_doc[term] = frequency



    doc_list=[doc1,doc2,doc3,doc4]
    mydoclist = [doc5,doc6,doc7,doc8]
    doc_term_matrix = []
    #i=1
    #for doc in doc_list:
        #print '-'*20
        #print 'doc%d' % i
        #for word in doc:
            #print '"%s":%f' % (word,tfidf(word,doc,doc_list))
        #i+=1

    #for word in sample_doc:
	#tfidf_scores[word]  = tfidf(word,sample_doc,doc_list)
	
    #for word in tfidf_scores:
	#print "This is the TFIDF ----->", tfidf_scores[word]
        
    for word in tfidf_scores:
        tfidf_sentence_scores[word] = tfidf_scores[word]

    vocabulary = build_lexicon(mydoclist)  #bulding Lexicon
    print vocabulary

    for doc in mydoclist:
	tf_vector = [termfreq(word, doc) for word in vocabulary]
	print doc, "--->", tf_vector
	print "\n"
	doc_term_matrix.append(tf_vector)

    doc_term_matrix_normalized = []

    for vec in doc_term_matrix:
	doc_term_matrix_normalized.append(normalizer(vec))

    my_idf_vector = [idf(word, doc_list) for word in vocabulary]
    print "\n"
    print "This is the idf-vector ---->",my_idf_vector
    print "\n"   
    
    tfidf_matrix = build_tfidf_matrix(my_idf_vector, doc_term_matrix_normalized)
    #print tfidf_matrix
    #print "\n"
    for vector in tfidf_matrix:
	#print "This is the tfidf vector ---->",vector
	print vector	
  
    print "\n"
    my_ref_len = len(my_idf_vector)

    cosine_similarity(tfidf_matrix,my_ref_len)

    my_sentences = sentence.extract_sentence("test3.txt")

    #for sentence in my_sentences:    
	#print "Sentence ------>", sentence

    for sentence in my_sentences:
	tfisf_sum = 0
	for word in sentence:
	    for word_score in tfidf_scores:
		if word == word_score:
		   tfisf_sum = tfisf_sum + tfidf_scores[word_score]
	tfidf_sentence_scores[sentence] = tfisf_sum

    #for sentence in tfidf_sentence_scores:
	#tfisf_scores[sentence] = float(tfidf_sentence_scores[sentence]/tfidf_sum(tfidf_scores))

    Y = pdist(tfidf_matrix)
    Z = linkage(Y)
    dendrogram(Z)
 
    show()


    


	
