#!/usr/bin/env python3

import sys
#import os
from collections import defaultdict
import re

def loadCreFloxDict():
    CFdict = {}
    with open('mini_term_cre-flox.tsv', 'r') as f:
        for line in f.readlines():
            l = line.strip().split('\t')
            for a in l[2].split('|'):
                CFdict[a.lower()] = l[1]
    return CFdict

def getNgram(wordList, n):
    for i in range(2, n):
        for j in range(len(wordList)-n+1):
            ngramTemp = "".join(wordList[j:j+n])
            if ngramTemp not in wordList:
                wordList.append(ngramTemp)
    return wordList

def processTokens(tokens):
    tmpTokens = tokens
    newTokens = []
    delNum = []
    for i in range(len(tokens)):
        if tokens[i] == '-':
            tmpTokens.append("".join(tokens[i-1:i+2]))
            for j in [i-1, i, i+1]:
                if j not in delNum:
                    delNum.append(j)
        elif tokens[i].lower() == '-cre':
            tmpTokens.append("".join(tokens[i-1:i+1]))
            for k in [i-1, i]:
                if k not in delNum:
                    delNum.append(k)
    for m in range(len(tmpTokens)):
        if m not in delNum:
            newTokens.append(tmpTokens[m])
    return newTokens

def CreFloxStat(paper_processed):
#    dic = loadCreFloxDict()
    cre_stat = defaultdict(int)
    with open(paper_processed, 'r') as f:
        lines = f.readlines()
        pmid = lines[0].strip()
        for line in lines[1:]:
            l = line.strip().split('\t')[1].split('; ')
            dellist = []
            new_l = []
            for m in range(len(l)):
                if re.match(r'^.+\-cre$', l[m].lower()):
                    cre_stat[l[m].lower()] += 1
                    dellist.append(m)
            for n in range(len(l)):
                if n not in dellist:
                    new_l.append(l[n])
            tokens = processTokens(new_l)
            for t in tokens:
                if t.lower().endswith('-cre'):
                    cre_stat[t.lower()] += 1
    for k,v in cre_stat.items():
        print(pmid+'\t'+k+'\t'+str(v))
#            word_3gram = getNgram(l, 3)
#            for word in word_3gram:
#                if word.lower() in dic:
#                    cre_stat[dic[word.lower()]] += 1
#    for k, v in cre_stat.items():
#        print(pmid+'\t'+k+'\t'+str(v))


CreFloxStat(sys.argv[1])


