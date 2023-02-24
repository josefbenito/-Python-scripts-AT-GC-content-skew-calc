#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#calculating GC skew values of all genes from the amphipod's mitogenome

input_file = open("Amphipods_mitochondrial_genes_more-amphipods.fasta","r")

output_file = open("GC_AT-content_skew_allgenes_more-amphipods.tsv","w")

output_file.write("Amphipod_gene\tA\tT\tG\tC\tLength_gene\tGC_percent\tAT_percent\tGC_skew\tAT_skew\n")

from Bio import SeqIO

for nucleotide in SeqIO.parse(input_file,"fasta"):
    amphipod_gene = nucleotide.name
    A_count = nucleotide.seq.count("A")
    T_count = nucleotide.seq.count("T")
    G_count = nucleotide.seq.count("G")
    C_count = nucleotide.seq.count("C")
    length_gene = len(nucleotide)
    GC_percent = float(G_count + C_count)/length_gene*100
    AT_percent = float(A_count + T_count)/length_gene*100    
    GC_skew = float(G_count - C_count)/(G_count + C_count)
    AT_skew = float(A_count - T_count)/(A_count + T_count)  
    output_line = "%s\t%i\t%i\t%i\t%i\t%i\t%f\t%f\t%f\t%f\n" % (amphipod_gene,A_count,T_count,G_count,C_count,length_gene,GC_percent,AT_percent,GC_skew,AT_skew)
    output_file.write(output_line)
    
    print "\nAmphipod_gene: ", amphipod_gene
    print "A: ", A_count
    print "T: ", T_count
    print "G: ", G_count
    print "C: ", C_count
    print "GC%: ", GC_percent
    print "AT%: ", AT_percent
    print "GC_skew: ", GC_skew
    print "AT_skew: ", AT_skew
    
output_file.close()
input_file.close()