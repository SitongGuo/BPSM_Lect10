#! /usr/local/bin/python3

import os
os.chdir("/localdisk/home/s2221039/LectureExercises/Lect_10/")
with open("DNA_sequence.txt") as dna_file:
	dna_seq = dna_file.read()
print(dna_seq)
dna_A_count=dna_seq.count("A")
dna_T_count=dna_seq.count("T")
dna_length=len(dna_seq)
dna_A=dna_A_count/dna_length
dna_T=dna_T_count/dna_length
print(dna_A,dna_T)

