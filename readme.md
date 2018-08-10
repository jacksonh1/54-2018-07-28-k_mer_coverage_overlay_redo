## redo of k-mer overlay with experimental data

### need data (k-mers vs. SRR1520311-Galaxy53-Rm_rRNA_on_data_17)
- **`--norc -v 2 -p 4 -m 1 `**
- **`--norc -a -v2 -p4`**

## filepaths (coverage csv's and alignment logfiles)
```
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/v3_simreads_FILTERED1-alignment--norc-v2-p4-m1/YMR186W-v3_simreads_FILTERED1--norc-v2-p4-m1.csv'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/v3_simreads_FILTERED1-alignment--norc-a-v2-p4/YMR186W-v3_simreads_FILTERED1--norc-a-v2-p4.csv'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/SRR1520311-Galaxy53-Rm_rRNA_on_data_17/SRR1520311-Galaxy53-Rm_rRNA_on_data_17-alignment--norc-a-v2-p4/YMR186W-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-a-v2-p4.csv'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/SRR1520311-Galaxy53-Rm_rRNA_on_data_17/SRR1520311-Galaxy53-Rm_rRNA_on_data_17-alignment--norc-v2-p4-m1/YMR186W-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-v2-p4-m1.csv'

'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/v3_simreads_FILTERED1-alignment--norc-v2-p4-m1/logfile.txt'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/v3_simreads_FILTERED1-alignment--norc-a-v2-p4/logfile.txt'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/SRR1520311-Galaxy53-Rm_rRNA_on_data_17/SRR1520311-Galaxy53-Rm_rRNA_on_data_17-alignment--norc-a-v2-p4/logfile.txt'
'../../alignments/flash-alignments-do_not_touch/final_alignments3/Yeast/orf_coding-FILTERED1/SRR1520311-Galaxy53-Rm_rRNA_on_data_17/SRR1520311-Galaxy53-Rm_rRNA_on_data_17-alignment--norc-v2-p4-m1/logfile.txt'
```
- copy them all with `./copy_script.sh`
