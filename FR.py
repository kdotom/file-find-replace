#!/usr/bin/env python3
import fileinput
import csv

filename = 'example.txt'
csvfilename = 'replacement-words.csv'


with open(csvfilename, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in csvreader:
		print(', '.join(row))
		text_to_search = row[0]
		replacement_text = row[1]
		with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
		    for line in file:
		        print(line.replace(text_to_search, replacement_text), end='')

