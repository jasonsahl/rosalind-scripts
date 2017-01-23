#!/usr/bin/python

import sys

# recurrence relation 
# 
# given stopGeneration and numPairsProduced
# Fn = Fn-1 + (Fn-2 * numPairsProduced)
# Start with gen 1 and gen 2, both have 1 rabbitPair (since it takes 1 gen/month for the pair to mature to breeding age)
# so the "start" is gen 3, and we decide to repeat (recurse or loop) x amount of times until we get to the stopGeneration (nth generation)
#

stopGeneration = int(sys.argv[1])
numPairsProduced = int(sys.argv[2])

def breedRabbits():
	nMinus2Gen = 1
	nMinus1Gen = 1

	for i in range(stopGeneration - 2):
		nGen = nMinus1Gen + (nMinus2Gen * numPairsProduced)
		nMinus2Gen = nMinus1Gen
		nMinus1Gen = nGen

	return nGen


def main():
	print breedRabbits()

if __name__ == '__main__':
	main()