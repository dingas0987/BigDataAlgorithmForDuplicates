import math
import sys
import psutil
import os 
from os import path, write
from file_utils import *

amount_of_ram_to_be_used = (psutil.virtual_memory().free * 0.05)
dupe_loc = set()
curr_set = set()
dupe_count = 0
total_lines = 0
fill_set_line_count = 0
offset_by = 0
leftover = 0

def get_total_lines(filename):
    global total_lines
    global leftover
    total_lines = get_line_count(filename)
    print("# of lines in file:", total_lines)
    leftover = total_lines

def fill_set(file_input):
    global fill_set_line_count
    global dupe_count
    global offset_by
    global leftover
    fill_set_dupe_count = 0
    with open(file_input, 'r') as input:
        for line in input:
            if curr_set.__sizeof__() < amount_of_ram_to_be_used:
                fill_set_line_count += 1
                if fill_set_line_count > offset_by:
                    if fill_set_line_count in dupe_loc:
                        continue
                    if line in curr_set:
                        dupe_loc.add(fill_set_line_count)
                        fill_set_dupe_count += 1
                    else:
                        curr_set.add(line)
    print("# of dupes while filling set:", fill_set_dupe_count)
    dupe_count += fill_set_dupe_count
    offset_by = fill_set_line_count
    fill_set_line_count = 0
    leftover = total_lines - offset_by
    print("leftover:", leftover)
    compare_to_file(file_input)

def compare_to_file(file_input):
    with open(file_input, 'r') as input:
        global dupe_count
        counter = 0
        line_count = 0
        for line in input:
            line_count += 1
            if line_count > offset_by:
                if line_count in dupe_loc:
                    continue
                if line in curr_set:    
                    dupe_loc.add(line_count)
                    counter += 1
    print("# of dupes in rest of file that is contained in current set", counter)
    dupe_count += counter
    print("current # of duplicates found", dupe_count)
    curr_set.clear()

# Pretty much unused/ slower than just writing to a new file
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

def writeFile(filename, output):
    line_count = 0
    with open(filename, 'r') as readfile:
        with open(output, 'w') as writefile:
            for line in readfile:
                line_count += 1
                if line_count in dupe_loc:
                    continue
                else:
                    writefile.writelines(line)

# Counter starts at 1 since the first line in the text file is line 0
# counter is then incremented for each removal in the array of duplicates
def delete_lines(filename):
    dupe_loc.sort()
    counter = 1
    for x in dupe_loc:
        counter += 1
    dupe_loc.clear()

def main(filename, output):
    add_newline_if_missing(filename)
    get_total_lines(filename)
    while(leftover != 0):
        fill_set(filename)
        if offset_by == total_lines:
            break
    writeFile(filename, output)
    print("total dupes", dupe_count)