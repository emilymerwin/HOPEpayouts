#! /usr/bin/env python
import csv  
import json  

# Open the CSV  
f = open( 'HOPEpayouts.csv', 'rU' )  
elementArr = [] #put our school elements where we can find them
keyArr = [] #have a parallel key array so we can look up the index we want from the elementArr
tree = {}
# Change each fieldname to the appropriate field name. I know, so difficult.  
#reader = csv.DictReader( f, fieldnames = ( "school","fiscyear","tuitionfees","hopepays","studentowes","source","notes" )) #doing it this way will put row 1 into your data - exclude fieldnames to use row 1 as fieldnames
reader = csv.DictReader( f, dialect='excel')
holder = 0
for i, row in enumerate(reader):
	#subtree = tree
	#subtree = Subtree2()
	school1 = row['school']
	try:
		holder = keyArr.index(school1)
		print holder
		#temp = 

		#subtree[i] = temp
		#print subtree
		#print "try"
	except ValueError:

		subtree = {}
		print "EXCEPT!"
		#subtree['school'] = row['school']
		#subtree = Subtree2()
		elementArr.append(subtree)
		keyArr.append(school1)
		holder = len(keyArr)-1
		print holder
		elementArr[holder]['school'] = {}
		elementArr[holder]['school']['name'] = row['school']
		#elementArr[holder]['school']['source'] = row['source']
		elementArr[holder]['school']['notes'] = row['notes']
		elementArr[holder]['school']['lines'] = {}
		elementArr[holder]['school']['lines']['hopepays'] = []
		elementArr[holder]['school']['lines']['tuitionfees'] = []
		elementArr[holder]['school']['lines']['studentowes'] = []
		#elementArr[holder]['school']['holder'] = holder
		#print subtree
		#print "except"
	
	
	#tempArr = []
	elementArr[holder]['school']['lines']['studentowes'].append(round(float(row['studentowes'])))
	elementArr[holder]['school']['lines']['tuitionfees'].append(round(float(row['tuitionfees'])))
	elementArr[holder]['school']['lines']['hopepays'].append(round(float(row['hopepays'])))
	#lines.append(round(float(row['hopepays'])))
	#lines.append(round(float(row['tuitionfees'])))
	#lines.append(round(float(row['studentowes'])))
	#elementArr[holder]['school']['years'].append(tempArr)
	#elementArr[holder]['school']['fiscyear']['year'] = row['fiscyear']
	#elementArr[holder]['school']['years']['hopepays'] = round(float(row['hopepays']))
	#elementArr[holder]['school']['years']['tuitionfees'] = round(float(row['tuitionfees']))
	#elementArr[holder]['school']['years']['studentowes'] = round(float(row['studentowes']))

tree = elementArr

	#tree[row] = subtree
	#print subtree
	#subtree = subtree[i]
		#subtree[row['school']]
	#for i, cell in enumerate(row):
		#if cell == row['school']:

			#if cell not in subtree:
				#if i<len(row)-1:
					#subtree[cell] = {}
				#else:
					#subtree[cell] = row[cell]
                #subtree[cell] = {} if i<len(row)-1 else row[cell]
			#subtree = subtree[cell]
		#else:
			#subtree[cell] = row[cell]
		#subtree = subtree[cell]"""

		
	#print cell
#print elementArr
print json.dumps(tree, indent=4)
#for row in reader:
	#print row['school']
	#school1 = row['school']
	#try:
		#holder = keyArr.index(school1)
		#school = elementArr[holder]
		#print "Yay"
	#except ValueError:
		#school = doc.createElement('school')
		#print school
		
	#print row
# Parse the CSV into JSON  
#out = json.dumps( [ row for row in reader ] )  
out = json.dumps(tree, indent=4)
print "JSON parsed!"  
# Save the JSON  
f = open( 'CSVtoJSONwithParsing_brackets.json', 'w')  
f.write(out)  
print "JSON saved!"