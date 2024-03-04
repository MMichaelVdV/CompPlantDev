# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:19:21 2024
"""

from Bio import SeqIO

original_file = "Lotus_japonicus.fa"
corrected_file = "Lotus_japonicus_corrected.fa"

with open(original_file) as original, open(corrected_file, 'w') as corrected:
    records = SeqIO.parse(original_file, 'fasta')
    for record in records:
        #print(record.id)         
        geneId = (record.id).split('.')[0]
        record.description = "gene:" + str(geneId)
        #print(record.description) 
        SeqIO.write(record, corrected, 'fasta')
