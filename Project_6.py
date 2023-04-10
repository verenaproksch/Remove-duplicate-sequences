#!/usr/bin/env python3
"""
Script to remove duplicate sequences from an input_file and put them into an output_file,
counts the number of sequences
Writer: Verena Proksch
Created on: 10.04.2023
"""
# import argparse and os.path modules
import argparse #used to parse to use command line arguments while running the script
import os.path #provides functions to work with file paths and directories

# #Parse command line arguments
parser = argparse.ArgumentParser(description="remove duplicate sequences")#create object called parser to parse command line arguments
parser.add_argument("input_file", help="input FASTA file")#command line argument for input of FASTA file
parser.add_argument("output_file", help="output FASTA file")#command line argument for output of FASTA file
parser.add_argument("-ci", "--count_input", action="store_true", help="print number of sequences in the input file")#command line argument to count number of sequences in input_file
parser.add_argument("-co", "--count_output", action="store_true", help="print number of unique sequences in the output file")#command line argument to count number of sequences in output_file
args = parser.parse_args()#parses command line arguments and stores them in object args

# Open the input file
with open(args.input_file) as f: #opens input_file
    lines = f.readlines() #read all lines in input_file, returns each line of input_file as an item in the list "lines"


# Parse the sequences and names from the input file
sequences = [] #List for all sequences
names = [] #List for all sequence names
for line in lines:
    if line.startswith(">"): #all headers start with ">"
        names.append(line.strip()) #appends all headers in list "names", .strip removes possible blank spaces
    else: #when line doesn't start with ">", it is a sequence
        sequences.append(line.strip().upper()) #appends all sequences to list "sequences", .strip to removes blank spaces, .upper returns all strings in capital characters

# Count the occurrences of each sequence
counts = {} #empty dictionary to count number of sequences
for i in range(len(sequences)):#for every sequence in list "sequences"

    sequence = sequences[i]#the current sequence
    name = names[i]#the name of the current sequence

    if sequence in counts:#if current sequence is already in the dictionary "counts"
        counts[sequence]["count"] += 1#increase the count value by 1
    else:#if the current sequence is not in the dictionary "counts"
        counts[sequence] = {"count": 1, "name": name}#name is added to "counts", together with the count "1"

# Open the output file and write the unique sequences
with open(args.output_file, "w") as f: #opens output_file in writing mode
    for sequence, info in counts.items():#iterates over each element in the dictionary "counts" 
        #sequences and infos are returned as a tuple,info is a dictionary name and count value 
        header = "{},{}x".format(info["name"], info["count"])#Create headers for the sequences, consisting of name and sequence count
        f.write(header + "\n")#write the header in the output_file, followed by line-break string
        f.write(sequence + "\n")#write the unique sequence in the output_file, followed by line-break string

# Print a summary of the number of sequences in the input and output files
num_sequences_original = len(sequences)#counts length of the list with all seuqnces from the original input_file, including the duplicates
num_sequences_unique = len(counts)#counts length of the list with unique sequences
if args.count_input: #if command line argument -ci is given
    print("Number of sequences in input file '{}': {}".format(args.input_file, num_sequences_original))#.format() formats specified values and inserts them inside the strings placeholder {};
    #The first curly bracket is replaced by the name of the input_file and the second by the number of sequences.

if args.count_output:#if command line argument -co is given
    print("Number of unique sequences in output file '{}': {}".format(args.output_file, num_sequences_unique))
    #The first curly bracket is replaced by the name of the output_file, the second by the number of unique sequences