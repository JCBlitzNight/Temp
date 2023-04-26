import pandas as pd
import json
from dataclasses import dataclass
from typing import List

# set the values for the TFDS criteria
c = 100  # minimum number of flows for a source to be considered
alpha = 0.5  # threshold for observed FSD entropy
eta1 = 10  # threshold for likelihood ratio to flag as scanner
eta0 = 0.1  # threshold for likelihood ratio to remove from Candidate

@dataclass
class Record:
    src_ip: str
    dest_ip: str
    dest_port: int
    action: str

# read the CSV file into a Pandas DataFrame
df = pd.read_csv('input.csv')

# create an empty dictionary to store the Source and Candidate hash tables
Source = {}
Candidate = {}

# iterate over each row in the DataFrame
for index, row in df.iterrows():
    # create a Record object from the row data
    record = Record(row['source_ip'], row['dest_ip'], row['dest_port'], row['action'])
    
    # add the Record object to the Source hash table
    if record.src_ip in Source:
        Source[record.src_ip]['flowcount'] += 1
    else:
        Source[record.src_ip] = {'flowcount': 1}
    
    # update the FSD entropy for the source in the Source hash table
    source_counts = [count['count'] for count in Source[record.src_ip]['counts']]
    source_counts.append(1)
    Source[record.src_ip]['counts'] = [{'count': count, 'freq': source_counts.count(count)/len(source_counts)} 
                                       for count in set(source_counts)]
    Source[record.src_ip]['fsd'] = -sum([count['freq']*math.log(count['freq'], 2) for count in Source[record.src_ip]['counts']])
    
    # update the likelihood ratio for the source in the Candidate hash table
    if Source[record.src_ip]['flowcount'] >= c:
        if record.src_ip not in Candidate:
            Candidate[record.src_ip] = 1
        else:
            ratio = Candidate[record.src_ip]
            if Source[record.src_ip]['fsd'] < alpha:
                ratio *= (1/Pr_Y1_H1)*((Source[record.src_ip]['flowcount']+1)/Pr_Y1_H0)
            else:
                ratio *= (1-Pr_Y1_H1)*Pr_Y0_H0/Source[record.src_ip]['flowcount']
            Candidate[record.src_ip] = ratio
            if ratio >= eta1:
                del Candidate[record.src_ip]
                # add the source to the selected_ips list to indicate it is a scanner
                selected_ips.append(record.src_ip)
            elif ratio <= eta0:
                del Candidate[record.src_ip]

# convert the selected_ips list to a JSON string
json_str = json.dumps(selected_ips)

# write the JSON string to a file
with open('output.json', 'w') as outfile:
    outfile.write(json_str)
