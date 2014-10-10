import re

def main(file_path,query):
   
    with open (file_path, "r") as myfile:
        data=myfile.read().replace('\n', '')
   
    #query = "dislocation"
   
    with open('listTogether.txt', 'w') as out:
         out.writelines(sorted([sentence + '.' for sentence in data.split('.') if query in sentence]))

    with open ('listTogether.txt', "r") as myfile:
         lines = [line.lower() for line in myfile]
    
    with open('listTogether_new.txt', 'w') as out:
         out.writelines(sorted(lines))

    punc=(",/;'?&-()")

    f = open('listTogether_new.txt', 'r')

    strp = [line.translate(None, punc) for line in f]
 
    with open('listTogether_new.txt', 'w') as out:
         out.writelines(sorted(strp))
   
    
        

   



    
