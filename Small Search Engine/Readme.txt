Instructions to Execute program:

1) Run the indexer.py program using the following command:
indexer.py tccorpus.txt index.out

This will generate an index.out file.

2) Run the BM25.py program using following command:
BM25.py index.out queries.txt 100 > results.eval

Output will be saved in results.eval file in the following format:

query_id Q0 doc_id rank BM25_score system_name

Short note on implementation of program is given is implementation.txt file

