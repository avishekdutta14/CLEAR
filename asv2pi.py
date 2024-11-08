#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Avishek Dutta, avishek.dutta@uga.edu
@requires: python3, pandas, numpy

Example syntax:

python asv_to_picrust.py -t taxonomy.tsv -p pred_metagenome_contrib.tsv -k K02588 K00399

"""

import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--taxonomy', help = 'Taxonomy file')

parser.add_argument('-p', '--predmeta', help = 'Predicted metagenome KEGG from PICRUST')

parser.add_argument('-k', '--keggid', type=str, nargs='*', help = 'KEGG ID')

args = parser.parse_args()

taxonomy = '{}'.format(args.taxonomy)
predmeta = '{}'.format(args.predmeta)
keggid = '{}'.format(args.keggid)

tax = pd.read_csv("{}".format(taxonomy), sep = '\t')

meta = pd.read_csv("{}".format(predmeta), sep = '\t')

merged_df = pd.merge(tax, meta, left_on='Feature ID', right_on='taxon')

for ko in eval(keggid):
    selected_kegg = merged_df[merged_df['function'] == "{}".format(ko)]
    selected_kegg.to_csv("asv_contributing_to_{}.csv".format(ko), index =False)
    print("The file is created for {}".format(ko))
