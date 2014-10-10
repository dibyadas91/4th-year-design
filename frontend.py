from bottle import route, run, debug, request
from operator import itemgetter
import os
import preprocessing1
from math import log
import string
import sentence
import word_freq
import tfidf
import math
import lower

@route('/', method='GET')


@route('/upload')
def upload():
    return '''
	<html>
	<head>
	<title>Query Focused Multi-Document Summarizer</title>
	<style type="text/css">
	/* Reset body padding and margins */
	body { margin:0; padding:0; }
	 
	/* Make Header Sticky */
	#header_container { background:#3399ff; border:1px solid #666; height:60px; left:0; position:fixed; width:100%; top:0; }
	#header{ line-height:60px; margin:0 auto; width:940px; text-align:center; }
	 
	/* CSS for the content of page. I am giving top and bottom padding of 80px to make sure the header and footer do not overlap the content.*/
	#container { margin:0 auto; overflow:auto; padding:80px 0; width:940px; }
	#content{}
	 
	/* Make Footer Sticky */
	#footer_container { background:#3399ff; border:1px solid #666; bottom:0; height:60px; left:0; position:fixed; width:100%; }
	#footer { line-height:60px; margin:0 auto; width:940px; text-align:center; }
	</style>
	</head>
	<body>
	<!-- BEGIN: Sticky Header -->
	<div id="header_container">
	    <div id="header">
		<font size=7>Query Focused Multi-Document Summarizer</font>
	    </div>
	</div>
	<!-- END: Sticky Header -->
	 
	<!-- BEGIN: Page Content -->
	<div id="container">
	    <div id="content">
		 <form action="/upload" method="post" enctype="multipart/form-data">
  		 <center>Query:      <input type="text" name="query" /></center>
		 <br><center>Degree of Dissimilarity:      0<input type="range" step="any" name="degree" min="0" max="1">1</center></br>
  		 <br><center>Select a file: <input type="file" name="upload" /></center></br>
  		 <br><center><input type="submit" value="Start upload" /></center></br>
		</form>
	    </div>
	</div>
	<!-- END: Page Content -->
	 
	<!-- BEGIN: Sticky Footer -->
	<div id="footer_container">
	    <div id="footer">
		 
	    </div>
	</div>
	<!-- END: Sticky Footer -->
	</body>
	</html>'''

   

@route('/upload', method='POST')
def do_upload():
    category   = 'txt'
    upload     = request.files.get('upload')
    query      = request.forms.get('query')
    degree     = request.forms.get('degree')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg', '.txt'):
        return 'File extension not allowed.'

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    with open(file_path, 'w') as open_file:
        open_file.write(upload.file.read())


    lower.main(file_path,query)

    my_sentences = sentence.extract_sentence('listTogether_new.txt') 
    my_sentences1 = sentence.extract_sentence('listTogether.txt')
    queriedSentences = preprocessing1.makeQueriedList(my_sentences,query)
    queriedSentences1 = preprocessing1.makeQueriedList(my_sentences1,query)

    words = preprocessing1.wordList(my_sentences)

    queryDictList = preprocessing1.buildQueryDictList(queriedSentences,words)
  
    myLexicon = tfidf.build_lexicon(queriedSentences)

    print myLexicon
  
    if not myLexicon:
       return ''' Error: Query Word not in document '''

    tfidfMatrix = preprocessing1.buildTfidfMatrix(queriedSentences, myLexicon,queryDictList)
  
    degree1 = float(degree)
    (updatedtfidfMatrix,queriedSentences) = preprocessing1.dendrogramBuild(tfidfMatrix,queriedSentences,degree1)

    output = preprocessing1.printSummary(updatedtfidfMatrix,queriedSentences)

    return '{0}'.format(output)



    
run(host='localhost', port=8080, debug=True)
