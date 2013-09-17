#! /usr/bin/env python
import csv  
import json  
#this file will succesfully convert csv to its json equivalent
# Open the CSV  
f = open( 'HOPEpayouts.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
#reader = csv.DictReader( f, fieldnames = ( "school","fiscyear","tuitionfees","hopepays","studentowes","source","notes" )) #doing it this way will put row 1 into your data - exclude fieldnames to use row 1 as fieldnames
reader = csv.DictReader( f, dialect='excel')

# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print "JSON parsed!"  
# Save the JSON  
f = open( 'hope.json', 'w')  
f.write(out)  
print "JSON saved!"