#!//Users/Jackson/miniconda3/bin/python

'''
Created by: Jackson Halpin
Date: 5/15/18
'''

import numpy as np
import pandas as pd
import glob
import os
np.set_printoptions(suppress=True)
import sys
import os
# %%
# ==============================================================================
# // TITLE
# ==============================================================================

# input1 = './m1v2/YMR186W-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-m1-v2-p4.csv'
# input2 = './m1v2/YPL240C-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-m1-v2-p4.csv'
# base = os.path.basename(Input_name)
# basenoext = os.path.splitext(base)[0]
input1 = str(sys.argv[1])
input2 = str(sys.argv[2])
input3 = str(sys.argv[3])
# %%
# ==============================================================================
# // input and merge along alignment_position
# ==============================================================================

df1 = pd.read_csv(input1)
gene1 = '_' + 'data'
df2 = pd.read_csv(input2)
gene2 = '_' + 'kmers' 

df3 = pd.merge(df1, df2, on='alignment_position',
               how='outer', suffixes=(gene1, gene2))
df3 = df3.sort_values('alignment_position')

df3['identity'] = df3['sequence' + gene1] != df3['sequence' + gene2]
df3.identity = df3.identity.apply(int)

# %%
# ==============================================================================
# // TITLE
# ==============================================================================

df3.to_csv(input3, index=False)
