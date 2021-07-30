'''
Possible idea: Get the first 1 million lines from a text file
Put the 1 million lines into a set to check if there is a dupe within it

Compare each line in that set to the rest of the file to see if there are
duplicates in there

Might be too slow
'''

import sys
import psutil
import os 
from os import path

# Get Available RAM
percent_of_mem_avail = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
amount_of_ram_to_be_used = (psutil.virtual_memory().free * 0.5) / (10**9)

curr_set = set()

# Fill the Set until it hits the RAM limit
def fill_set(file_input):
    with open(file_input, 'r') as input:
        for line in input:
            if(curr_set.__sizeof__() < amount_of_ram_to_be_used):
                if(line not in curr_set):
                    curr_set.add(line)
            else:
                continue

# Compare the current Set to the original File
# and remove the duplicate in the file
# if it is found
def compare_to_file(file_input):
    with open(file_input, 'r') as input:
        dupe_count = 0
        for line in input:
            if(line in curr_set):
                dupe_count += 1
                #REMOVE DUPLICATE LINE
                remove_duplicate(line)
            else:
                continue

# Delete line from file
def remove_duplicate(file_input, line_selection):
    print("delete the line", line_selection)