#! /usr/local/bin/python3

from __future__ import division
import os
os.chdir("/localdisk/home/s2221039/LectureExercises/Lect_10/")
with open("genomic_dna.txt") as gen_file:
        gen_seq = gen_file.read()
coding1=gen_seq[0:63]
coding2=gen_seq[90:]
cod_seq=coding1+coding2
print((len(cod_seq)/len(gen_seq))*100)

coding1=coding1.upper()
coding2=coding2.upper()
intron=gen_seq[63:90]
intron=intron.lower()
final_seq=coding1+intron+coding2
print(final_seq)

