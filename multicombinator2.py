#!/usr/bin/python
__author__ = 'ryman1'
#combines a dictionary with itself a specfed number of times using the specified splitting charater(s)
print "combines a dictionary with itself a specfied number of times with the specified splitting character(s)"
print "Usage 'multicombinator.py wordlistfile number-or-repetitions(>2) [splitting character]'"
import sys
import glob

wordfileargument = glob.glob(sys.argv[1])[0]
depthgoal = int(sys.argv[2])
try:
    splitter = sys.argv[3]
except:
    splitter = ''

currentword = ''

def addlist(currentword, depthin):
    wordfile = open(wordfileargument,'r')
    depthin += 1
    for line in wordfile.readlines():
        if depthin < depthgoal and depthin > 1:
            addlist(currentword + splitter + line.rstrip(), depthin)
        elif depthin == 1:
            addlist(line.rstrip(), depthin)
        else:
            try:
                print currentword + splitter + line.rstrip()
            except IOError:
                pass
    wordfile.close()
    return


addlist(currentword, 0)