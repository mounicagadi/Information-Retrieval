__author__ = 'Mounica Gadi'

import sys
import json

dict_docs = {} #dictionary to store the docid and values from the given corpus
words_freq = {} # it is the dictionary which stores in the inverted indexer of the given corpus
indexer_dump = [] # store the indexer created from the corpus and the length of the documents and can be written on a file
dict_len = {} # store the length the of each docid present in the corpus i.e the count of values for a
              # given docid

def indexer(dict_docs):
    # The below mentioned 3 lines of code removes all the values which contains only digits
    # from the dict_docs. This dictionary will now have values which are words and alphanumeric
    # but not only digits
    for key,values in dict_docs.iteritems():
        new_values = filter(lambda x: not x.isdigit() ,values)
        dict_docs[key] = new_values

# The below block of code is for creating the indexer. It checks if the values in dict_docs
# are present in a new dictionary words_freq. It picks a single term from values every time
# and checks if the term is present in words_freq dictionary. If present, then it checks if the docid is present
# for that particular term. If docid is present , increments it by 1 else initializes the value
# to 1. If term is only not present, initializes the value for
#  a particular docid to be 1.
    for docid,values in dict_docs.iteritems():
        for term in values:
            if term in words_freq:
                if docid in words_freq[term]:
                    words_freq[term][docid] += 1
                else:
                     words_freq[term][docid] = 1
            else:
                words_freq[term] = {docid:1}
# calculating the length of the documents for each docid and returning the 2 dictionaries
        length = len(dict_docs[docid])
        dict_len[docid] = length

    return words_freq , dict_len

def main(input,output):
# The input file will be the corpus given to us. The below lines of code will help in
# opening the file and splitting the file based on '#'. All the terms before # are considered
# to be the docids and terms after # are considered to be the values of that particular docid

    text_file = open(input,'r')
    corpus = text_file.read()
    lines = corpus.split('#')[1:] # split the corpus based on '#'
    for line in lines:
        values = line.split()
        doc_id = values[0]
        dict_docs[doc_id] = values # dict_docs is a dictionary which stores the docid and its values

    indexer_dump = indexer(dict_docs)
    outfile = open(output,'w+') # opening the outfile and dumping the inverted list of index
                                #  created out of dict_docs
    json.dump(indexer_dump,outfile)

    print "The index.out file is ready \n"
    print "Algorithm completed"

if __name__ ==  "__main__":
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print "Starting the indexer: \n"
        main(arg1,arg2)
    except:
        print "Error occured"
        exit(0)



