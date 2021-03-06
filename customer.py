from person import person
from person import make_ssn
import random as r
from datetime import datetime as dt

def make_routingNumber():
	'''Creates and returns a fake routing number for a checking account as a string Ex: 123456789'''
	routing_number = ''
	for n in range(9):
		routing_number += str(r.randint(0, 9))
	return routing_number

class customer(person):
	customer_number = 0
	acct_number_addition = 123456789

	def __init__(self):
		person.__init__(self)
		customer.customer_number += 1
		self.customer_number = customer.customer_number
		self.account_number = customer.customer_number + customer.acct_number_addition		# Fake account number is created made and assigned
		self.routing_number = make_routingNumber()
		self.balance = 0
		self.mutual_fund_acct_balance = 0
		self.metal_gem_fund_acct_balance = 0
		self.crypto_acct_balance = 0
		self.outstanding_balance = 0
		customer.acct_number_addition += r.randint(10, 50)
		person.customer_list.append(self)
		self.__deleted_customer = False				# Set to true only if the manager deletes a customer. True value disables bank privileges.
		
		print('\nChecking account has been opened for {}.'.format(self.name))

		self.__pin = input('\nSet a 4-digit pin: ')
		while len(self.__pin) != 4 or not self.__pin.isnumeric():
			self.__pin = input('\nPlease enter a 4-digit pin: ')

		deposit = input('\nWhat is the initial deposit?: $')

		done = False
		while not done:	
			try:
				deposit = float(deposit)
				if deposit > 10:
					self.balance += deposit
					done = True
				else:
					deposit = input('\nEnter an amount over $10 to deposit: $')
			except:
				deposit = input('\nEnter a valid amount to deposit: $')

		print('\nDone.\n')

	def __mfAccountStatus(self):
		'''Prints status of a customer's mutual fund investment account, if it has a balance. Tells them the estimated rate of return for this investment type.'''
		
		estimated_return_rate = 1.067 	# Estimated annual return rate for mutual funds.

		print('\n\n    Your current mutual fund account balance is ${}. With an estimated return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.mutual_fund_acct_balance, '.2f'), estimated_return_rate, format(self.mutual_fund_acct_balance*estimated_return_rate, '.2f')))

	def __mgfAccountStatus(self):
		'''Prints status of a customer's precious metal & gem fund investment account, if it has a balance. Tells them the estimated rate of return for this investment type.'''
		
		estimated_return_rate = 1.081	# Estimated annual return rate for this precious metal and gem fund.
		
		print('\n\n    Your current precious metal & gem fund account balance is ${}. With an estimated return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.metal_gem_fund_acct_balance, '.2f'), estimated_return_rate, format(self.metal_gem_fund_acct_balance*estimated_return_rate, '.2f')))
	
	def __cryptoAccountStatus(self):
		'''Prints status of a customer's cryptocurrency investment account, if it has a balance. Tells them the estimated rate of return for this investment type.'''
		
		estimated_return_rate = 1.143	 # Estimated annual return rate for cryptocurrency investment.
		
		print('\n\n    Your current cryptocurrency account balance is ${}. With an estimated return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.crypto_acct_balance, '.2f'), estimated_return_rate, format(self.crypto_acct_balance*estimated_return_rate, '.2f')))
		
	def __str__(self):
		'''String representation of a customer includes some basic personal information, account info, and financial info.'''
		return 'Customer: {}\n\nD.O.B: {}/{}/{}\n\nAddress: {}\n\nAccount Number: {}\n\nRoutingNumber: {}\n\nChecking Balance: {}\n\nNet Worth: ${}'.format(self.name, self.birthdate.month, self.birthdate.day, self.birthdate.year, self.address, str(self.account_number).zfill(12), self.routing_number, self.balance, format(self.balance + self.crypto_acct_balance + self.mutual_fund_acct_balance + self.metal_gem_fund_acct_balance, '.2f'))

	def __deposit(self):
		'''Customer can make a deposit to their checking account. This function is called when visiting an ATM or by a teller'''
		deposit = input('\nAmount to deposit: $')
		
		done = False
		while not done:	
			try:
				deposit = float(deposit)
				if deposit > 0:
					self.balance += deposit
					done = True
				else:
					deposit = input('\nEnter a positive amount to deposit: $')
			except:
				deposit = input('\nEnter a valid amount to deposit: $')

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)

	def __withdrawal(self):
		'''Customers can make a withdrawal from their checking account. This function is called when visiting an ATM or by a teller'''
		self.__check_balance()
		amount = input('\nAmount to withdraw: $')

		done = False
		while not done:
			try:
				amount = float(amount)
				if 0 <= amount <= self.balance:
					self.balance -= amount
					done = True
				elif amount > self.balance:
					amount = input('\nAmount exceeds balance. Enter a valid amount to withdraw: $')
				else:
					amount = input('\nEnter a positive amount to withdraw: $')
			except:
				amount = input('\nEnter a valid, whole-dollar amount to withdraw: $')
		

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)	

	def __check_balance(self):
		'''Prints the balance of a customer's checking account. Called either at an ATM or by a teller'''
		print('\n\nChecking Account Balance: $%.2f' % self.balance)

	def __CheckOutstandingBalance(self):
		'''Prints a customer's outstanding balance with I.L.L & Sons'''

		print('\n\nOutstanding balance: ${}'.format(format(self.outstanding_balance, '.2f')))



	def atm(self):
		'''Simulates an ATM environment, allowing active customer's to check their balance and deposit or withdraw money.'''

		if not self.__deleted_customer:
			pin = input('\nEnter your pin: ')
			incorrect_attempts = 0
			access_granted = False
			while not access_granted and incorrect_attempts < 3:
				if pin == self.__pin:
					access_granted = True			# The only way for access to be granted is for the pin to be entered correctly within the first 3 tries
				else:
					incorrect_attempts += 1
					pin = input('\nTry again: ')

			if not access_granted:
				print('\nToo many failed attempts.')


			if access_granted:
				print('\n\n     Welcome to I.L.L & Sons Bank!     \n\n      Thank you for choosing us!')
				print('\n\n       How may we help you?\n')

			done = False
			while not done and access_granted:
				choice = input('\nEnter (1):      Balance Inquiry  \n\nEnter (2):      Deposit  \n\nEnter (3):      Withdrawal  \n\nEnter (4):      Exit\n\nEntry: ')
				if choice == '1':
					self.__check_balance()

					y_n = input('\nWould you like another transaction? (yes/no): ')

					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\nWould you like another transaction? (yes/no): ')

					if y_n.lower() in ['no', 'n']:
						done = True
					
				elif choice == '2':
					self.__deposit()

					y_n = input('\nWould you like another transaction? (yes/no): ')

					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\nWould you like another transaction? (yes/no): ')

					if y_n.lower() in ['no', 'n']:
						done = True

				elif choice == '3':
					y_n = input('\n\nThere will be a $3 surcharge for ATM withdrawals. Accept this fee? (yes/no): ')

					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nAccept 3 surcharge for ATM withdrawal? (yes/no): ')

					if y_n.lower() in ['yes', 'y']:
						self.balance -= 3
						self.__withdrawal()

					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\nWould you like another transaction? (yes/no): ')

					if y_n.lower() in ['no', 'n']:
						done = True

				elif choice == '4':
					print('\n\n    Goodbye!')
					done = True
				else:
					choice = input('\nEnter (1):      Balance Inquiry  \n\nEnter (2):      Deposit  \n\nEnter (3):      Withdrawal  \n\nEnter (4):      Exit\n\nEntry: ')

		else:

			print('\n\n    Only active customers can use this ATM.')

	def talk(self):
		'''A customer will introduce themself by name.'''
		greeting = r.randint(1, 2)		# Pick a random greeting
		if greeting == 1:
			print("Hello. I'm {} {}. I chose I.L.L & Sons because it has that classic, hometown bank feel".format(self.first_name, self.last_name))
		elif greeting == 2:
			print("Hey. My name\'s' {}.".format(self.first_name))