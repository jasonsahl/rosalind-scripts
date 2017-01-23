#!/usr/bin/python

import sys

# Mendel's first law

dom    = int(sys.argv[1])
hetero = int(sys.argv[2])
rece   = int(sys.argv[3])

total = dom + hetero + rece

def probabilities():
	domSquared = float(dom)/total * float(dom-1)/(total-1) * 1

	domCrossHetero = float(dom)/total * float(hetero)/(total-1) * 2 * 1

	domCrossRece = float(dom)/total * float(rece)/(total-1) * 2 * 1

	heteroSquared = float(hetero)/total * float(hetero-1)/(total-1) * 3/4

	heteroCrossRece = float(hetero)/total * float(rece)/(total-1) * 2 * 1/2

	receSquared = float(rece)/total * float(rece-1)/(total-1) * 0

	return domSquared + domCrossHetero + domCrossRece + heteroSquared + heteroCrossRece + receSquared

def main():
	print "%.5f" % probabilities()

if __name__ == "__main__":
	main()