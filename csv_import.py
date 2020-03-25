import csv

orig_csv_file = 'BDSOpportunityAssignment.csv'
new_csv_file = 'editedOppsList.csv'

with open(orig_csv_file, 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open(new_csv_file, 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='-')

		for line in csv_reader:
			csv_writer.writerow(line)