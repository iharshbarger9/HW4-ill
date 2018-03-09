'I consulted the official python 3.6.4 documentation'
import random as r
from datetime import datetime as dt

def make_ssn():
	'''Creates and returns a fake Social Security Number Ex: 123-45-6789'''
	ssn = ''
	for x in range(9):
		if x in [3, 5]:
			ssn += '-'
		ssn += str(r.randint(0, 9))
	return ssn

def make_routingNumber():
	'''Creates and returns a fake routing number Ex: 123456789'''
	routing_number = ''
	for n in range(9):
		routing_number += str(r.randint(0, 9))
	return routing_number

class person():
	customer_list = [] 		# Every instance of customer will be added to this list
	past_customer_list = []

	def __init__(self):
		print('\n\n\n Welcome to I.L.L & Sons Bank!\n')

		self.employee_permissions = False
		self.manager_permissions = False
		self.advisor_permissions = False

		print("\nLet's set up the profile.")

		'''Have user input person's name and check for valid entries'''
		self.first_name = input('\nFirst name: ')
		while len(self.first_name) == 0 or not self.first_name.isalpha():		
			self.first_name = input('Enter a valid first name: ')

		self.middle_name = input('\nMiddle name (Press enter if unavailable): ')
		while len(self.middle_name) != 0 and not self.middle_name.isalpha():
			self.middle_name = input('Enter a valid middle name, if available: ')

		self.last_name = input('\nLast name: ')
		while len(self.last_name) == 0 or not self.last_name.isalpha():
			self.last_name = input('Enter a valid last name: ')

		self.name = '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

		'''Have user input person's birthdate'''
		birthdate = input('\nDate of birth: mm/dd/YYYY: ')

		'''Verify correct birthday format'''
		valid_birthdate = False
		while not valid_birthdate:
			try:
				self.birthdate = dt.strptime(birthdate, '%m/%d/%Y').date()
				valid_birthdate = True
			except:
				 birthdate = input('\nEnter a valid birthdate. mm/dd/YYYY: ')

		'''Calculate age'''
		self.age = dt.today().year - self.birthdate.year
		if self.birthdate.month > dt.today().month:
			self.age -= 1
		elif self.birthdate.month == dt.today().month and self.birthdate.day > dt.today().day:
			self.age -= 1

		'''Have user input person's address and check for valid entries'''
		self.street_address = input('\nStreet address (Ex: 3 South Market St.): ')
		while not len(self.street_address.split(' ')) >= 2 or not self.street_address.split(' ')[0].isdigit():
			self.street_address = input('Enter a valid street address: ')

		self.city = input('\nCity: ')
		while not len(self.city) >= 2:
			self.city = input('Enter the city: ')

		self.state = input('\nState (Ex: PA): ').upper()
		while self.state not in ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']:
			self.state = input('\nEnter a valid US state abbreviation: ').upper()

		self.zip_code = input('\nZip Code: ')
		while len(self.zip_code) != 5:
			self.zip_code = input('\nEnter a 5-digit zip code: ')

		self.address = '{} {}, {} {}'.format(self.street_address, self.city, self.state, self.zip_code)

		'''Create a fake Social Security number for the person'''
		self.__ssn = make_ssn()
		print('\nSSN is on file.')

	def talk(self):
		'''Person will talk and introduce themselves'''
		raise NotImplementedError('Talk method for subclass has not been implemented yet')