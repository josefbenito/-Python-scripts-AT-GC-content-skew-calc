#!/usr/bin/env python2
# -*- coding: utf-8 -*-

input_file = open("mtgenomes_all_remaining_amphipods.fasta","r")

output_file = open("mtgenomes_GC_AT-content_skew.tsv","w")

output_file.write("Amphipods\tA\tT\tG\tC\tLength_mtgenome\tGC_percent\tAT_percent\tGC_skew\tAT_skew\n")

from Bio import SeqIO

for nucleotide in SeqIO.parse(input_file,"fasta"):
    amphipod_name = nucleotide.name
    A_count = nucleotide.seq.count("A")
    T_count = nucleotide.seq.count("T")
    G_count = nucleotide.seq.count("G")
    C_count = nucleotide.seq.count("C")
    length_mito = len(nucleotide)
    GC_percent = float(G_count + C_count)/length_mito*100
    AT_percent = float(A_count + T_count)/length_mito*100
    GC_skew = float(G_count - C_count)/(G_count + C_count)
    AT_skew = float(A_count - T_count)/(A_count + T_count)  
    output_line = "%s\t%i\t%i\t%i\t%i\t%i\t%f\t%f\t%f\t%f\n" % (amphipod_name, A_count, T_count, G_count, C_count, length_mito, GC_percent, AT_percent, GC_skew, AT_skew)
    output_file.write(output_line)
    
    print "\nAmphipod: ", amphipod_name
    print "A: ", A_count
    print "T: ", T_count
    print "G: ", G_count
    print "C: ", C_count
    print "Length_mtgenome: ", length_mito
    print "GC%: ", GC_percent
    print "AT%: ", AT_percent
    print "GC-skew: ", GC_skew
    print "AT-skew: ", AT_skew
    
output_file.close()
input_file.close()