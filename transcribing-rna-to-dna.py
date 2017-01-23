#!/usr/bin/env python

import string

f = open('rosalind_rna.txt', 'r')
s = f.read()

# test
#s = "GATGGAACTTGACTACGTAAATT"

print s.replace("T", "U")
