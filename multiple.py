from bottle import route, run, debug, template, request
from operator import itemgetter
import os
import preprocessing1
from math import log
import string
import sentence
import word_freq
import tfidf
import math

@route('/', method='GET')


@route('/upload')
def upload():
    return '''
        <body style="background-color:yellow;">
        <h2 style="background-color:red;">This is a heading</h2>
        <p style="background-color:green;">This is a paragraph.</p>
        <form action="/upload" method="post" enctype="multipart/form-data">
  	<br><center>Select a file: <input type="file" name="upload" multiple></center></br>
  	<br><center><input type="submit" value="Start upload" /></center></br>
	</form>
	</body>
    '''

@route('/upload', method='POST')
def do_upload():
    category   = request.forms.get('category')
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
    #return "File successfully saved to '{0}'.".format(save_path)

    #TODO: Code for calling the preprocessing python file and preprocessing the file
    return 0
    

    

    


    
run(host='localhost', port=8080, debug=True)
