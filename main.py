import tfidf


def main():

   table = tfidf.tfidf()
   table.addDocument("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "alpha"])
   table.addDocument("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
   table.addDocument("baz", ["kilo", "lima", "mike", "november"])

   print table.similarities (["alpha", "bravo", "charlie"]) # => [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]

if __name__ == '__main__':
  main()


def garbabeRemoval(sentence):

   string = "!s*imo*w!?!?!@@~n"
   newString = ''

   validLetters = "abcdefghijklmnopqrstuvwxyz"

   for word in sentence:
       for char in string:
           if char in validLetters:
              newString += char
 	      print newString
