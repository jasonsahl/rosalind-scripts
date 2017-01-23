#!/usr/bin/python

# GC Content
#
# given a file with up to 10 DNA strings in FAFSA format (each at most 1kbp in length)
# find the DNA string with the highest GC content percentage and print the name of the string as well as the percentage
#
# === Sample Dataset
#
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
#
#
# === Sample output
#
# Rosalind_0808
# 60.919540

import re, sys

# get file
def getSeqsAndNamesFromFile():
	"""Gets FAFSA sequences and corresponding names from file (the first argument)"""
	f = open(sys.argv[1], 'r')
	lines = []
	sequences = []
	seqNames = []
	aSequence = ""

	for line in f:
		lines.append(line.strip())
	f.close()

	for index, line in enumerate(lines):
		test = re.search('>(\w+_\d{4})', line)
		if test is None:
			aSequence += line
		else:
			if (len(aSequence) > 0):
				sequences.append(aSequence)
				aSequence = ""
			seqName = test.group(1)
			seqNames.append(seqName)
	# last sequence
	sequences.append(aSequence)

	return sequences, seqNames

def getHighestGC(seqList, nameList):
	maxSeqPercent = 0.0
	for index, seq in enumerate(seqList):
		currSeqPercent = calculateGCPercentage(seq)
		if currSeqPercent > maxSeqPercent:
			maxSeqPercent = currSeqPercent
			indexOfMax = index

	return indexOfMax, maxSeqPercent 

# calculate GC content
def calculateGCPercentage(seq):

	numGC = seq.count('C') + seq.count('G')

	percentageGC = 100 * (float(numGC) / len(seq))
	return percentageGC

def printPercentage(percGC):
	# print the percentage with precision of 6 decimal places
	print ("%.6f" % percGC)

def printList(aList):
	for item in aList:
		print "list item: {}".format(item)

def main():
	seqs, names = getSeqsAndNamesFromFile()
	index, percent = getHighestGC(seqs, names)
	print names[index]
	printPercentage(percent)

if __name__ == '__main__':
	main()

