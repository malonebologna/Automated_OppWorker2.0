import csv

with open('BDSOpportunityAssignment.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='\n')

		for line in csv_reader:
			csv_writer.writerow(line)

			for line in csv_reader:
				print(line['NAICS Code Assigned'])
				print(line['Additional BDS NAICS codes'])