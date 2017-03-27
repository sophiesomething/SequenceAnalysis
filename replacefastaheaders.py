#!/usr/bin/env python3

# 20170327 - Sophie Andrews

# Script for changing the header names in a fasta file. 

# fasta.txt = your list of sequences in fasta format (plain text, UTF-8).
# newheaders.txt = your list of new header names, each on a new line (plain text, UTF-8). 
# newfasta.txt = where your new fasta file will be saved


fasta= open('fasta.txt','r')
newnames= open('newheaders.txt','r')
newfasta= open('newfasta.txt', 'w')

for line in fasta:
    if line.startswith('>'):
        newname= newnames.readline()
        newfasta.write(newname)
    else:
        newfasta.write(line)
        print (line)

fasta.close()
newnames.close()
newfasta.close()