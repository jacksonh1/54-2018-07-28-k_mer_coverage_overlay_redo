import re

files=[

'./files/YMR186W-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-a-v2-p4.csv',
'./files/YMR186W-SRR1520311-Galaxy53-Rm_rRNA_on_data_17--norc-v2-p4-m1.csv',
'./files/YMR186W-v3_simreads_FILTERED1--norc-a-v2-p4.csv',
'./files/YMR186W-v3_simreads_FILTERED1--norc-v2-p4-m1.csv'

]

pattern = re.compile(r'(.{7})(-SRR1520311|-v3_simreads_FILTERED1).*?--norc(-\w{1,2}-\w{2}-\w{2})\.csv')

file_params = {}
for i in files:
    match1 = re.search(pattern,i)
    file_params[i] = match1.groups()

# %%

''.join(file_params[i])
