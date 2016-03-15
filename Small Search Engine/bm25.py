__author__ = 'Mounica Gadi'

# constants

from math import log
import json
from operator import itemgetter
import sys

k1=1.2
b=0.75
k2=100

#Relevance information
R = 0.0
r = 0

#calculating BM25 score
# n = no of docs containing the term
# f = frequency of a term in a particular document
# qf = query frequency of the term
# r = relevant documents containing the term
# R = relevance information
# dl = length of the document
# avdl = average length of the document
# N = Total no of documents in the collection

def calc_score(n,f,qf,N,dl,avdl):
    K=k1*((1-b)+b*(float(dl)/float(avdl)))
    term_1=log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))
    term_2=((k1 + 1) * f)/(K + f)
    term_3=((k2+1)*qf)/(k2+qf)
    return term_1 * term_2 * term_3

def calc_average_length(doc_lengths): # calculates the average document length
     sum = 0
     for l in doc_lengths.values():
         sum += l
     avg = float(sum)/float(len(doc_lengths))
     return avg

# The below block of code calculates the scores of the document based on the
# terms in the given query
def bm_for_query(words,query,doc_lengths):
    doc_scores = {}
    qf = 1
    N = len(doc_lengths) # calculates the total length of the document
    for w in query:
        if w in words:
            term_val = words[w] #storess the docid and frequencies of a particular word
            for docid,freq in term_val.iteritems():
                    n = len(term_val)
                    score = calc_score(n,freq,qf,N,doc_lengths[docid],calc_average_length(doc_lengths)) # calculate the score
                    if docid in doc_scores : #scoring of the document
                        doc_scores[docid] += score
                    else:
                        doc_scores[docid] = score
    return doc_scores

def main(index,queries,max_doc):

    #query_file = queries
    index_file = open(index,'r')
    retrieve = json.load(index_file) # loads the index file
    words = retrieve[0] # contains the inverted index of the corpus
    doc_lengths = retrieve[1] # contains the docid and their length
    print "Loaded index.out file \n"

# reads the queries from the file
# and splits them based on new line break.
# Then they will be split into terms and are stored in a list
    f=open(queries)
    lines = f.read()
    line = lines.split("\n")
    query_lst= [x.rstrip().split() for x in line]
    print "Processed the queries \n"

    result = []
    for q in query_lst:
        result.append(bm_for_query(words,q,doc_lengths)) # calculates the document scores for each query in the list
    print "Calculated the document scores for the queries \n"

    print "Printing the document scores rank wise \n"
    query_id = 1 #initializing the query id to be 1
    doc_count = int(max_doc)
    for r in result:
        #sorting of the document based on the scored for each term in decreasing order
        sorted_list = sorted(r.iteritems(),key= itemgetter(1),reverse=True)
        rank = 1
        for i in sorted_list[:doc_count]:
            tmp = (query_id, i[0], rank, i[1])
            print '{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tMounica'.format(*tmp)
            rank += 1
        query_id += 1


if __name__=='__main__':
    try:
        print "BM25 Implementation : \n"
        index = sys.argv[1]
        queries = sys.argv[2]
        docs = sys.argv[3]
        main(index,queries,docs)
        print " Algorithm completed"
    except:
        print "Error occured"
        exit(0)


