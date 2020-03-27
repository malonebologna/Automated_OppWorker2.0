
def clean_OppsList():
	import csv

	orig_csv_file = 'BDSOpportunityAssignment.csv'
	new_csv_file = 'cleanOppsList.csv'

	with open(orig_csv_file, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)

		with open(new_csv_file, 'w') as new_file:
			fieldnames=['Entry #',
						'BDS',
						'BDS Email Address',
						'Opportunity Title',
						'Solicitation Number',
						'Agency',
						'Response Date',
						'Set Aside',
						'NAICS Code Assigned',
						'Additional BDS NAICS codes',
						'Industry',
						'Keyword Suggestions',
						'Link to Opportunity on FedBizOpps, DIBBS, NECO, etc',]

			csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

			csv_writer.writeheader()

			for line in csv_reader:
				del line['Date Created']
				del line['Date Updated']
				del line['IP Address']
				del line['Solicitation Email Addresses']
				del line['Office']
				del line['Location']
				del line['Notice Type']
				del line['PSC / FSC Code']
				del line['Estimated Value (Enter 25,000.00 if unknown)']
				del line['Response Date']
				del line['Synopsis - Do not list the entire opportunity.  Just the basic synopsis - keep it short.']
				del line['Contracting Office Address']
				del line['Place of Performance']
				del line['Most likely "winners" who will be notified separately by BDP.  Must include email addresses - if it does not include email addresses - and they are not in the lookup based on NAICS codes - the notification will not be sent to them.']
				del line['Trade associations - membership organizations - chambers - etc that will be notified separately by BDS']
				del line['Type']
				del line['Guaranteed Minimum Amount']
				del line['Task Order Solicitation Number']
				del line['Base Year + Number of Option Years (0 if none, total if applicable)']
				del line['Original Solicitation Number']
				del line['Prime Contractor Information']
				del line['Original Contractor Contract Numbers']
				del line['Primary Point of Contact']
				del line['Number of Contacts']
				del line['AA Assigned']
				del line['Manager Notes:']
				del line['AWARD INFORMATION']
				csv_writer.writerow(line)

def import_OppsList():
	pass

clean_OppsList()