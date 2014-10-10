

if __name__=='__main__':

    with open ("test1.txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

    query = "Mass"

    print [sentence + '.' for sentence in data.split('.') if query or query.lower() in sentence]

