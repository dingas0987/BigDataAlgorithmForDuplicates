# very incomplete

import math
import sys
import psutil
import os 
from os import path

# Get Available RAM
percent_of_mem_avail = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
amount_of_ram_to_be_used = (psutil.virtual_memory().free * 0.5)

# Store each section into a set
curr_set = set()

# Keep track of character length of entire file
char_tracker = 0

# Store Duplicate locations in a 2D array, first value is the line number
# and the second value is the length of the string 
dupe_loc = []

# Line count of set
fill_set_line_count = 0

# Counter used to insert into the dupe_loc array
arr_counter = 0

# Counter for Duplicates
dupe_count = 0

# Fill the Set until it hits the RAM limit
# NOTE: Lists/Sets do not grow in memory as the list/set grows
# The amount of space in memory increases when the list has a certain number of items
# i.e [1,2,3] ==> sizeof ==> 712 bytes, [1,2,3,4] ==> sizeof ==> 712 bytes
# [1,2,3,4,5,6,7,8] ==> sizeof == 1024 bytes, [1,2,3,4,5,6,7,8,9,10,11] ==> sizeof ==> 1388 bytes
def fill_set(file_input):
    global fill_set_line_count
    global char_tracker
    global arr_counter
    global dupe_count
    with open(file_input, 'r') as input:
        line = input.readline()
        while curr_set.__sizeof__() < amount_of_ram_to_be_used:
            char_tracker = len(line) + 1
            if line in curr_set:
                dupe_loc.insert(arr_counter, [fill_set_line_count, len(line)])
                arr_counter += 1
                dupe_count += 1
            else:
                curr_set.add(line)
            line = input.readline()
            fill_set_line_count += 1


# Compare the current Set to the original File
# and remove the duplicate in the file
# if it is found
def compare_to_file(file_input):
    with open(file_input, 'r') as input:
        global char_tracker
        global arr_counter
        global dupe_count
        line_count = 0
        for line in input:
            if line_count < fill_set_line_count:
                continue
            elif line in curr_set:
                dupe_loc.insert(arr_counter, [line_count, len(line)])
                arr_counter += 1
                dupe_count += 1
            line_count += 1
    print("# of duplicates", dupe_count)


# Function will remove the lines based on the dupe_loc array
def removeLine(fileinput):
    for x in dupe_loc:
        removeLineHelper(fileinput, x[0])
        decrement_line()  

# Delete line from file
def removeLineHelper(file_input, line_selection):
    fro = open(file_input, "r")

    current_line = 0
    while current_line < line_selection:
        fro.readline()
        current_line += 1

    seekpoint = fro.tell()
    frw = open(file_input, "r+")
    frw.seek(seekpoint, 0)

    # read the line we want to discard
    fro.readline()

    # now move the rest of the lines in the file 
    # one line back 
    chars = fro.readline()
    while chars:
        frw.writelines(chars)
        chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()

def decrement_line():
    # Remove from duplicate location array
    del(dupe_loc[0])

    # Decrement line number for the elements left in the duplicate location array
    # Because everything is now shifted up by 1 line
    # Keep length of line
    for x in dupe_loc:
       x[0] = x[0] - 1