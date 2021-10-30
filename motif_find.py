#! /usr/local/bin/python3

import os
os.chdir("/localdisk/home/s2221039/LectureExercises/Lect_10/")
with open("DNA_sequence.txt") as dna_file:
        dna_seq = dna_file.read()
print(dna_seq)
motif="GAATTC"
print(dna_seq.count(motif))
print(dna_seq.find(motif))
print(len(dna_seq))#no space
print(len(dna_seq)-dna_seq.find(motif)-1)
