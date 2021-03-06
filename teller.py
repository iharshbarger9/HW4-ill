from employee import *
import random as r

print("teller change")

class teller(employee):
	def __init__(self):
		employee.__init__(self)
		
	def ServeCustomer(self, other):
		'''Teller gives the customer the option to check their balance, make a deposit or withdrawal, transfer funds from an investment account to checking account, or make a payment on their outstanding balance. The main functionality of a bank teller'''
		if not other._customer__deleted_customer:

			print('\n\n    Hello there, {}! Hope you are doing well!\n\n    How can I help you today?'.format(other.first_name))
			
			done = False
			while not done:
				choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal from your checking account  \n\nEnter (4) to transfer funds from an investment account to your checking account   \n\nEnter (5) to make a payment on your outstanding balance \n\nEnter (6) to be reminded of your pin\n\nEnter (7) to say goodbye\n\nEntry: ')
				
				if choice == '1':
					other._customer__check_balance()

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True

				elif choice == '2':
					other._customer__deposit()

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True

				elif choice == '3':
					other._customer__withdrawal()

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True

				elif choice == '4':
					self.__TransferFromInvestmentAccount(other)

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True

				elif choice == '5':
					self.__PaymentOnOutstandingBalance(other)

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True

				elif choice == '6':
					print('\n\n    {}, your pin is {}. This time, I recommend you write it down so you don\'t forget again.'.format(other.first_name, other._customer__pin))

					y_n = input('\n\nIs that all for today? (yes/no): ')
					while y_n not in ['yes', 'y', 'no', 'n']:
						y_n = input('\n\nIs that all for today? (yes/no): ')
					if y_n.lower() in ['yes', 'y']:
						done = True
				
				elif choice == '7':
					print('\nGoodbye!')
					done = True
				else:
					choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal from your checking account  \n\nEnter (4) to transfer funds from an investment account to your checking account   \n\nEnter (5) to make a payment on your outstanding balance \n\nEnter (6) to be reminded of your pin\n\nEnter (7) to say goodbye\n\nEntry: ')
				print('\nHave a nice day!')

		else:

			print('\n\n    {}, your accounts with us are not active. To reactivate them, you can contact a manager.'.format(other.first_name))

	def __TransferFromInvestmentAccount(self, other):
		'''Helps the customer transfer funds from an investment account to their checking account, for a %5 fee. Called when a customer selects this option with a teller'''

		if other.mutual_fund_acct_balance == 0 and other.metal_gem_fund_acct_balance == 0 and other.crypto_acct_balance == 0:
			print('\n\n    Right now, you don\'t have any investment accounts with us! To open investment accounts, you should talk to a Financial Advisor.')

		if other.mutual_fund_acct_balance > 0:
			other._customer__mfAccountStatus()
			
			y_n = input('\n\n    We charge 5% of the amount to be transferred to transfer funds out of an investment account. Would you still like to transfer funds from this account to your checking account? (yes/no): ')
			while y_n not in ['yes', 'y', 'no', 'n']:
				y_n = input('\n\n    Accept fee and transfer from your mutual fund investment account? (yes/no): ')
			
			if y_n in ['yes', 'y']:
				amount = input('\n\n    How much would you like to transfer?\n\nAmount: $')
				
				done = False
				while not done:
					try:
						amount = float(amount)
						if 0 <= amount <= other.mutual_fund_acct_balance:
							other.mutual_fund_acct_balance -= amount
							other.balance += 0.95 * amount
							print('\n\n    Done.')
							print('\n\nNew Mutual Fund Account Balance: ${}\nNew Checking Account Balance: ${}'.format(other.mutual_fund_acct_balance, other.balance))
							done = True
						
						elif amount > other.mutual_fund_acct_balance:
							amount = input('\n\n    Transfer amount can\'t exceed your ${} balance.\n\nAmount: $'.format(other.mutual_fund_acct_balance))

						elif amount < 0:
							amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')

					except:
						amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')

		if other.metal_gem_fund_acct_balance > 0:
			other._customer__mgfAccountStatus()

			y_n = input('\n\n    We charge 5% of the amount to be transferred to transfer funds out of an investment account. Would you still like to transfer funds from this account to your checking account? (yes/no): ')
			while y_n not in ['yes', 'y', 'no', 'n']:
				y_n = input('\n\n    Accept fee and transfer from your precious metal & gem fund investment account? (yes/no): ')
			
			if y_n in ['yes', 'y']:
				amount = input('\n\n    How much would you like to transfer?\n\nAmount: $')
				
				done = False
				while not done:
					try:
						amount = float(amount)
						if 0 <= amount <= other.metal_gem_fund_acct_balance:
							other.metal_gem_fund_acct_balance -= amount
							other.balance += 0.95 * amount
							print('\n\n    Done.')
							print('\n\nNew Precious Metal & Gem Fund Account Balance: ${}\nNew Checking Account Balance: ${}'.format(other.metal_gem_fund_acct_balance, other.balance))
							done = True
						
						elif amount > other.metal_gem_fund_acct_balance:
							amount = input('\n\n    Transfer amount can\'t exceed your ${} balance.\n\nAmount: $'.format(other.metal_gem_fund_acct_balance))

						elif amount < 0:
							amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')

					except:
						amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')


		if other.crypto_acct_balance > 0:
			other._customer__cryptoAccountStatus()

			y_n = input('\n\n    We charge 5% of the amount to be transferred to transfer funds out of an investment account. Would you still like to transfer funds from this account to your checking account? (yes/no): ')
			while y_n not in ['yes', 'y', 'no', 'n']:
				y_n = input('\n\n    Accept fee and transfer from your cryptocurrency investment account? (yes/no): ')
			
			if y_n in ['yes', 'y']:
				amount = input('\n\n    How much would you like to transfer?\n\nAmount: $')
				
				done = False
				while not done:
					try:
						amount = float(amount)
						if 0 <= amount <= other.crypto_acct_balance:
							other.crypto_acct_balance -= amount
							other.balance += 0.95 * amount
							print('\n\n    Done.')
							print('\n\nNew Cryptocurrency Account Balance: ${}\nNew Checking Account Balance: ${}'.format(other.crypto_acct_balance, other.balance))
							done = True
						
						elif amount > other.crypto_acct_balance:
							amount = input('\n\n    Transfer amount can\'t exceed your ${} balance.\n\nAmount: $'.format(other.crypto_acct_balance))

						elif amount < 0:
							amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')

					except:
						amount = input('\n\n    Enter a valid amount to transfer.\n\nAmount: $')

	def __PaymentOnOutstandingBalance(self, other):
		'''Helps the customer make a payment on their outstanding balance, if they have one. Called when a customer selects this option with a teller'''
		print('\n\n    Current Outstanding Balance: ${}'.format(other.outstanding_balance))

		if other.outstanding_balance == 0:
			print('\n\n    Congratulations, {}! You do not have an outstanding balance.'.format(other.first_name))
		
		elif other.outstanding_balance > 0:
			if other.balance == 0:
				print('\n\n    You have no funds to make a payment on your outstanding balance. Please come back when you do.')
			
			elif other.balance > 0:
				done = False
				while not done:
					try:
						payment = float(payment)
						if 0 <= payment <= other.balance and 0 <= payment <= other.outstanding_balance:
							other.balance -= payment
							other.outstanding_balance -= payment
							print('\n\n    Thank you for the payment!')
							print('\n\nNew Outstanding Balance: ${}\nNew Checking Account Balance: ${}'.format(format(other.outstanding_balance, '.2f'), format(other.balance, '.2f')))
							done = True
							
						elif payment > other.balance:
							payment = input('\n\nYou don\'t have that much in your checking account to make a payment on your outstanding balance.\n\nPayment: $')
				
						elif payment > other.outstanding_balance:
							payment = input('\n\n    Your outstanding balance is less than that.\n\nPayment: $')
				
						elif payment < 0:
							payment = input('\n\n    Please enter a positive payment.\n\nPayment: $')

					except:
						payment = input('\n\n    Please enter a valid payment.\n\nPayment: $')

	def talk(self):
		'''Teller will introduce themselves one of three ways.'''
		greeting = r.randint(1, 3)		# Pick a random greeting

		if greeting == 1:
			print("Hello! I'm {} {}, been a teller here for a few years now.".format(self.first_name, self.last_name))
		elif greeting == 2:
			print("Hiya! My name is {} {}. I\'m one of the tellers here at I.L.L. & Sons. I\'m here to help the customers.".format(self.first_name, self.last_name))
		elif greeting == 3:
			print("Good day! I'm {} {}. I'd be happy to help you.".format(self.first_name, self.last_name))
