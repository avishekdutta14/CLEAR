# Comprehensive Lab Evaluation for Amplicon Results (CLEAR)

#### This repository is dedicated to downstream analysis of amplicon results from different tools

## asv2pi.py 

This script is for linking and filtering desired genes based on KEGG orthologs from the result of QIIME2 and PICRUSt2
You will need **taxonomy.qza** file from QIIME2 and **pred_metagenome_contrib.tsv** from PICRUSt2

To generate **pred_metagenome_contrib.tsv** the file, please use the following script.

```
picrust2_pipeline.py -s asv-sequences/dna-sequences.fasta -i feature-table/feature-table.biom -o picrust2_out_pipeline_stratfied -p 30 --stratified
```

**taxonomy.qza** is an output for the following script

```
qiime feature-classifier classify-sklearn \
  --i-classifier ../database/silva-138-99-515-806-nb-classifier.qza \
  --i-reads asv-sequences.qza \
  --o-classification taxonomy.qza
```
**N.B.:** You can use your own database for the analysis. We have used the Silva 138 database for this script. 

First, you will need to convert the **taxonomy.qza** file to a .tsv file using the following command

```
qiime tools export \
  --input-path taxonomy.qza \
  --output-path exported-taxonomy
```

You will find your **taxonomy.tsv** file inside the exported-taxonomy folder. Once you have the two input files and want to understand which taxonomic groups are contributing to the KEGG orthologs, you will use the following syntax

```
python asv2pi.py -t path_for_taxonomy_file/taxonomy.tsv -p path_for_asv_contribution_file/pred_metagenome_contrib.tsv -k K00161 K00162
```
You can use as many KEGG orthologs in the script. It will create separate files and report microbes contributing to each KEGG ortholog in a CSV file.
