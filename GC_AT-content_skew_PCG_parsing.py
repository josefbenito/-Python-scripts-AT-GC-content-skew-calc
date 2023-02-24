#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#parsing GC skew values of protein coding genes alone from GC skew calculation table

InFile = file("GC_AT-content_skew_allgenes.tsv","r") 
OutFile = file("GC_AT-content_skew_PCG_parsed.tsv","w")

a = InFile.readlines() 
z = len(a)

import re
def exact_Match(text,genes):
    result = re.findall('\\b'+'\W'+genes+'\\b',text)
    if len(result)>0:
        return True
    else:
        return False

genes = ['-;nad1','-;nad4','-;nad4l','-;nad5','+;atp6','+;atp8','+;cob','+;cox1','+;cox2','+;cox3','+;nad2','+;nad3','+;nad6']
samples = ['MP25A','MP28A','MP53A','MP26A','MP31B','Sty_indentatus','Gam_duebeni','Gam_fossarum','Eulimnogammarus-verrucosus','Eulimnogammarus-cyaneus','Caprella-scaura','Caprella-mutica','Brachyuropus-grewingkii','Bahadzia_jaraguensis']

x = len(genes)
w = len(samples)

for j in range(z):
    spl = a[j].split()
    y = len(spl)
    for i in range(y): 
        if 'Amphipod' in str(spl[i]):
            output = a[j].split()
            rec = ""
            rec += "\t".join(output[1: ])
            print "Amphipod\tGene\t",rec
            OutFile.write("Amphipod\tGene\t")
            OutFile.write(rec)
        for k in range(x):
            for l in range(w):
                if exact_Match(str(spl[i]),genes[k]):
                    if samples[l] in str(spl[i]):
                        output = a[j].split()
                        rec = ""
                        rec += "\t".join(output[1: ])
                        print samples[l],"\t",genes[k],"\t",rec
                        OutFile.write("\n")
                        OutFile.write(samples[l])
                        OutFile.write("\t")
                        OutFile.write(genes[k])
                        OutFile.write("\t")
                        OutFile.write(rec)
          
InFile.close()
OutFile.close()
