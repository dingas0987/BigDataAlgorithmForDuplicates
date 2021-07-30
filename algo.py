'''
GOAL: BE ABLE TO DELETE DUPLICATE LINES IN A TEXT FILE THAT CANNOT BE PLACED INTO MEMORY

SOME NOTES:
- Query OS for RAM support (48 GB)
- Fill the set with half available RAM
    - Or first 1m lines
- Check for duplicates that exist in set
    - If (size_of(set) < (ram_support/2):
        - If it doesn't exist, add to set
    - else: continue
'''

import sys
import psutil
import os 
from os import path

percent_of_mem_avail = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
amount_of_ram_to_be_used = (psutil.virtual_memory().free * 0.5) / (10**9)
#curr_set = set()
curr_set = []

def ram_avail():
    percent_of_mem_avail = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    amount_of_ram_to_be_used = (psutil.virtual_memory().free * 0.5) / (10**9)
    print(str(amount_of_ram_to_be_used) + ' GB'); 

def duplicates_in_set(search_set):
    dupe_count = 0
    for line in search_set:
        if line in search_set:
            dupe_count += 1
        else:
            continue

# Fill set up to the limit (amount of ram that can be used)
# if it does not exist in the set
def set_size(file_input):
    with open(file_input, 'r') as input:
        for line in input:
            if(curr_set.__sizeof__() < amount_of_ram_to_be_used):
                if(line not in curr_set):
                    #curr_set.add(line)
                    curr_set.append(line)
            else:
                continue

# Compare contents in the set to the full file
def compare_to_file(file_input):
    with open(file_input, 'r+') as input_file:
        dupe_count = 0
        for line in input_file:
            if line in curr_set:
                dupe_count += 1
                #delete_dupe(line, file_input)
                #writeToFile(line)
            else:
                continue

# Plan A
# Delete the line that is the duplicate in the original file
def delete_dupe(line, file_input):
    with open(file_input, 'r+') as input_file:
        for file_line in input_file:
            if line == file_line:
                print("REMOVE THE LINE FROM THE FILE")

# Plan B
# Write the original lines in a new file
def writeToFile(file, text):
    # Create a file if it does not exist
    if not path.exists(file):
        with open(file, 'w', encoding='ISO-8859-1', errors='ignore') as createfile: 
            createfile.close()
    # Add the text to the new file
    with open(file, 'a') as newfile:
        newfile.write(text)
        newfile.close()

def remove_line(file, line):
    with open("target.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != line:
                f.write(i)
        f.truncate()
