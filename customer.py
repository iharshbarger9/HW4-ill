from person import person
from person import make_routingNumber
from person import make_ssn
import random as r
from datetime import datetime as dt

class customer(person):
	customer_number = 0
	acct_number_addition = 1234567

	def __init__(self):
		person.__init__(self)
		self.account_number = customer.customer_number + customer.acct_number_addition
		self.routing_number = make_routingNumber()
		self.balance = 0
		self.customer_number = customer.customer_number
		self.mutual_fund_acct_balance = 0
		self.metal_gem_fund_acct_balance = 0
		self.crypto_acct_balance = 0
		self.outstanding_balance = 0
		customer.customer_number += 1
		customer.acct_number_addition += r.randint(10, 50)
		person.customer_list.append(self)
		
		print('\nBank account has been opened for {}.'.format(self.name))

		self.__pin = input('\nSet a 4-digit pin: ')
		while len(self.__pin) != 4 or not self.__pin.isnumeric():
			self.__pin = input('\nPlease enter a 4-digit pin: ')

		deposit = input('\nWhat is the initial deposit?: $')
	
		while not deposit.isnumeric() or not float(deposit) > 0:
			deposit = input('\nEnter a valid amount to deposit: $')

		self.balance += float(deposit)

		print('\nDone.\n')

	def __mfAccountStatus(self):
		return_rate = r.normalvariate(1.067, 0.032)
		print('\n\n    Your current mutual fund account balance is ${}. Based on our estimates, with a return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.mutual_fund_acct_balance, '.2f'), format(return_rate, '.2f'), format(self.mutual_fund_acct_balance*return_rate, '.2f')))

	def __mgfAccountStatus(self):
		return_rate = r.normalvariate(1.08, 0.05)
		print('\n\n    Your current precious metal & gem fund account balance is ${}. Based on our estimates, with a return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.metal_gem_fund_acct_balance, '.2f'), format(return_rate, '.2f'), format(self.metal_gem_fund_acct_balance*return_rate, '.2f')))
	
	def __cryptoAccountStatus(self):
		return_rate = r.normalvariate(1.14, 0.12)
		print('\n\n    Your current cryptocurrency account balance is ${}. Based on our estimates, with a return rate of {}%, after this year, your balance should be about ${}.'.format(format(self.crypto_acct_balance, '.2f'), format(return_rate, '.2f'), format(self.crypto_acct_balance*return_rate, '.2f')))

	def __str__(self):
		return 'Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(self.name, self.birthdate.month, self.birthdate.day, self.birthdate.year, self.address, str(self.account_number).zfill(12), self.routing_number, self.balance)

	def __deposit(self):
		done = False
		deposit = input('\nAmount to deposit: $')
		while not done:	
			if not deposit.isnumeric():
				deposit = input('\nEnter a valid amount to deposit: $')
			elif float(deposit) < 0:
				deposit = input('\nEnter a positive amount to deposit: $')
			else:
				self.balance += float(deposit)
				done = True

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)

	def __withdrawal(self):
		done = False
		amount = input('\nAmount to withdraw: $')
		while not done:	
			if not amount.isnumeric():
				amount = input('\nEnter a valid amount to withdraw: $')
			elif not float(amount) > 0:
				amount = input('\nEnter a positive amount to withdraw: $')
			elif not float(amount) <= self.balance:
				amount = input('\nAmount exceeds balance. Enter a valid amount to withdraw: $')
			else:
				self.balance -= float(amount)
				done = True

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)	

	def __check_balance(self):
		print('Balance: $%.2f' % self.balance)

	def __CheckOutstandingBalance(self):
		print('Outstanding: ${}'.format(format(self.outstanding_balance, '.2f')))


	def atm(self):
		pin = input('\nEnter your pin: ')
		incorrect_attempts = 0
		access_granted = False
		while not access_granted and incorrect_attempts <= 3:
			if pin == self.__pin:
				access_granted = True
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
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '2':
				self.__deposit()
				y_n = input('\nWould you like another transaction? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '3':
				y_n = input('\nThere will be a $3 surcharge for ATM withdrawals. Accept this fee? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					self.balance -= 3
					self.__withdrawal()
				y_n = input('\nWould you like another transaction? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '4':
				done = True
			else:
				choice = input('\nEnter (1):      Balance Inquiry  \n\nEnter (2):      Deposit  \n\nEnter (3):      Withdrawal  \n\nEnter (4):      Exit\n\nEntry: ')

	def talk(self):
		print("Hello! I'm {}".format(self.first_name))