# Variables
orig_opps_file = 'BDSOpportunityAssignment.csv'
clean_opps_file = 'cleanOppsList.csv'
orig_act_file = 'ACT_Contacts.csv'
clean_act_file ='cleanActContacts.csv'

#-----------------------------------------------------------

def clean_OppsData():
	import csv

	with open(orig_opps_file, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)

		with open(clean_opps_file, 'w') as new_file:
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
				del line['Response Date (test)']
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

#-----------------------------------------------------------				

def import_OppsList():
	import csv

	csv_file = open(clean_opps_file, 'r')
	csv_reader = csv.reader(csv_file)
	opps_List = []

	for row in csv_reader:
		opps_List.append({
			'Entry #':row[0],
			'BDS':row[1],
			'BDS Email Address':row[2],
			'Opportunity Title':row[3],
			'Solicitation Number':row[4],
			'Agency':row[5],
			'Response Date':row[6],
			'Set Aside':row[7],
			'NAICS Code Assigned':row[8],
			'Additional BDS NAICS codes':row[9],
			'Industry':row[10],
			'Keyword Suggestions':row[11],
			'Link to Opportunity on FedBizOpps, DIBBS, NECO, etc':row[12]})
	
	return opps_List

#-----------------------------------------------------------

def clean_ActData():
	import pandas as pd
	contacts = pd.read_csv(orig_act_file)
	contacts=contacts.dropna(subset=['E-mail'])
	contacts.to_csv(clean_act_file,index=False)


#-----------------------------------------------------------

def import_ActDict():
	pass

#-----------------------------------------------------------

def main():
	# clean_OppsData()

	# for i in import_OppsList():
	# 		print(i)
	# 		print('\n')

	clean_ActData()

main()