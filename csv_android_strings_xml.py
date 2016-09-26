import csv

header = """<?xml version="1.0" encoding="utf-8"?>
<resources>
"""
footer = "</resources>"
item = """<string name="{0}">{1}</string>\n"""

strings = header

csv_file_name = "states.csv"
skip_header = True
with open(csv_file_name, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		name = row[0]
		value = row[1]
		strings = strings + item.format(name, value)

strings = strings + footer
print strings		


