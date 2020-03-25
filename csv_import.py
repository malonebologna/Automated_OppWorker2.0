import csv

csvFile = 'BDSOpportunityAssignment.csv'
with open(csvFile, 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for line in csv_reader:
		print(line)