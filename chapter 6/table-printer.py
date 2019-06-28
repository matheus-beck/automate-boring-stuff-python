#!/usr/bin/env python3
# This program formats and prints a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(tableData):
	columnWidth = []
	
	# Search for the largest string in each list:
	for i in range(len(tableData)):
		largestString = ''
		for j in tableData[i]:
			if len(j) > len(largestString):
				largestString = j
		# Sets the len of sting to a list of table width
		columnWidth.append(len(largestString))
	
	#print('col width= ', columnWidth)
	
	for i in range(len(tableData[1])):
		for j in range(len(tableData)):
			print(tableData[j][i].rjust(columnWidth[j]), end=' ')
		print()
			
printTable(tableData)