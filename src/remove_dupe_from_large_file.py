import math
import sys
import psutil
import os 
from os import path

dupe_loc = []
amount_of_ram_to_be_used = 2048
curr_set = set()
dupe_count = 0
total_lines = 0
fill_set_line_count = 0
offset_by = 0

def get_total_lines(filename):
    global total_lines
    with open(filename, 'r') as readfile:
        for line in readfile:
            total_lines += 1
    print("# of lines in file:", total_lines)

def fill_set(file_input, offset):
    global fill_set_line_count
    global dupe_count
    global offset_by
    with open(file_input, 'r') as input:
        for line in input:
            if curr_set.__sizeof__() < amount_of_ram_to_be_used:
                fill_set_line_count += 1
                if fill_set_line_count > offset:
                        if line in curr_set:
                            dupe_loc.append(fill_set_line_count)
                            dupe_count += 1
                        else:
                            curr_set.add(line)
    print("# of dupes:", dupe_count)
    print("fill set line counter: ", fill_set_line_count)
    offset_by = fill_set_line_count

def compare_to_file(file_input):
    with open(file_input, 'r') as input:
        global dupe_count
        line_count = 0
        for line in input:
            line_count += 1
            if line_count > offset_by:
                if line in curr_set:
                    dupe_loc.append(line_count)
                    dupe_count += 1
    print("# of duplicates", dupe_count) 

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

# Counter starts at 1 since the first line in the text file is line 0
# counter is then incremented for each removal in the array of duplicates
def delete_lines(filename):
    counter = 1
    for x in dupe_loc:
        removeLineHelper(filename, x-counter)
        counter += 1
    dupe_loc.clear()

#get_total_lines('sample3.txt')
#fill_set('sample3.txt', fill_set_line_count)
#compare_to_file('sample3.txt')
#fill_set('sample3.txt', fill_set_line_count)
#print("current set:", curr_set)
#print("duplicates located on lines", dupe_loc)
#print("size of set:", curr_set.__sizeof__())
#delete_lines('sample3.txt')

def main():
    filename = 'sample3.txt'
    get_total_lines(filename)
    fill_set(filename, offset_by)
    compare_to_file(filename)
    delete_lines(filename)

if __name__ == '__main__':
    main()