#!/usr/bin/python

# Locating substrings in dna string
#

import sys
import string

# s = "GATATATGCATATACTT"
s = sys.argv[1] 
# t = "ATAT"
t = sys.argv[2]

# sample output 2 4 10 (location of start of ATAT)

# personal note: s.count(t) will output 2. It does not count overlapping substrings

# def getMotifIndex(s, t):
# 	if s.find(t):
# 		foundIndex = s.find(t)
# 		print foundIndex + 1,
# 		getMotifIndex(s[foundIndex+1:], t)
# 	elif len(s) is 0:
# 		return
# 	else:
# 		print "{} not found in {}".format(t,s)
# 		return

def getMotifIndeces(s,t):
	for index, char in enumerate(s):
		substring = s[index:]
		if substring[0:len(t)] == str(t):
			print index+1,

def main():
	getMotifIndeces(s, t)

if __name__ == "__main__":
	main()