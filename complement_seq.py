#! /usr/local/bin/python3

import os
os.chdir("/localdisk/home/s2221039/LectureExercises/Lect_10/")
with open("DNA_sequence.txt") as dna_file:
        dna_seq = dna_file.read()
A_to_T=dna_seq.replace("A","t")
T_to_A=A_to_T.replace("T","a")
C_to_G=T_to_A.replace("C","g")
G_to_C=C_to_G.replace("G","c")
final_result=G_to_C.upper()
print(final_result)
