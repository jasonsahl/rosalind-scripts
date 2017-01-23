#!/usr/bin/python

import sys

origSequence = sys.argv[1]
#origSequence = "AAAACCCGGT"
newSequence = ""

key = { 'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G' }

counter = len(origSequence)

while (counter > 0):
	newSequence += key[ origSequence[counter-1] ]
	counter -= 1

print newSequence