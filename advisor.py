from employee import *
import random as r

class advisor(employee):

	def __init__(self):
		employee.__init__(self)
		self.advisor_permissions = True

	def __offer_loan(self, other):
		done1 = False
		amount = input("\n    You've chosen a great lender in I.L.L & Sons. How much would you like to borrow? The least amount you can borrow is $50\n\nAmount: ")

		while not done1:
			try:
				amount = float(amount)
				if amount >= 50:
					done1 = True
				else:
					amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')
			except:
				amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')


		period = input('\n    Over how long would you like to pay back the loan?\n    We can offer 1-year, 5-year, or 25-year loans.\n\nNumber of years: ')
		while not period.isnumeric() or period not in ['1', '5', '25']:
			period = input('\nWe can offer 1-year, 5-year, or 25-year loans only.\n\nWhich best suits you?\nNumber of years: ')
		period = int(period)

		interest_rate = 4 + r.randint(10, 70)/100

		accept = input('\n\n{}, we can offer you a {}-year loan of ${} at an interest rate of {}%. Would you like to accept this loan? (yes/no):  '.format(other.first_name, period, format(amount, '.2f'), interest_rate))
		if accept.lower() in ['yes', 'y']:
			other.balance += amount
			other.outstanding_balance += float(str(format((((1 + interest_rate / 100) ** period) * amount) - amount, '.2f')))
			other._customer__CheckOutstandingBalance()
			print('\n    Each year you will owe {} / {} = ${} on this loan'.format(format(other.outstanding_balance, '.2f'), period, format(other.outstanding_balance/period, '.2f')))
		else:
			print('\n    Okay. If you reconsider, please come back and we can talk again.')

	def __open_investment_account(self, other):
		
		if other.balance < 1000:
			print('\n\n\n\n    To open an investment account, you must have at least $1,000 in your account.')
			print('\n\n    Right now, it looks like you don\'t have enough to open an investment account with us. Once you accumulate more funds, please come back and we will talk more about your investment options.')
		else:
			print('\n\n\n\n    Okay, {}, so you would like to invest. Good idea in today\'s world. Right now, we have three investment options for you to consider. Our mutual fund is doing great these days. It is the safest investment for you to make.\n\nOr I could get you in on our precious metal & gem fund. Yeah, it is a little riskier, but the potential reward is even greater.\n\nYou ever heard of bitcoin? What about XRP\'s Ripple? Well if you are into cryptocurrencies, we can help you invest in those, too.\n\nThe choice is yours, {}.'.format(other.first_name, other.first_name))
			choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you aren\'t interested anymore.\n\nEntry: ')
			
			while choice not in ['1', '2', '3', '4']:
				choice = input('\n(1) Mutual Fund\n\n(2)Precious metal & gem\n\n(3)Cryptocurrencies\n\n(4)Nevermind\n\nEntry: ')
			
			''' Here the advisor will tell the customer about projected return rates based on our estimates and a normal probability model. Ex: You have a {}% chance of earning at least 3% back'''

			done = False

			while not done:

				if choice == '1':	# Mutual Fund

					return_rate = r.normalvariate(1.067, 0.032)		# Estimated normal model for mutual fund has mean = 1.067% and std dev = 0.032%
					y_n = input('\n\n    Our mutual fund consists of mostly S&P 500 stocks. Our expert fund managers predict that there is an 88% chance of earning at least 3% annually.\n\n    Want to invest in this? (yes/no): ')
					
					while y_n not in ['yes', 'y', 'no', 'n']:						
						y_n = input('\n\nInvest? (yes/no): ')

					if y_n in ['no', 'n']:						
						y_n = input('\n\n    Still considering the other investment options? (yes/no): ')
						
						while y_n not in ['yes', 'y', 'no', 'n']:							
							y_n = input('\n\nConsidering other investment options? \n\n(yes/no): ')

						if y_n in ['yes', 'y']:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass

						else:
							
							done = True

					elif y_n in ['yes', 'y']:
						
						print('\n    Great choice.')

						amount = input('\n\n    How much would you like to invest in the mutual fund, {}? The least we\'ll invest is $500.\n\nAmount: $'.format(other.first_name))
						done1 = False
						while not done1:
							try:
								
								amount = float(amount)
								
								if 500 <= amount <= other.balance:
									done1 = True
								
								else:
									amount = input('\nInvestment must be at least $500, but no more than your account balance.\n\nAmount: $')
							except:
								amount = input('\nEnter a valid amount over $500 to invest.\n\nAmount: $')

						other.balance -= amount
						other.mutual_fund_acct_balance += amount

						print('\n\n    I\'ve deposited {} to your mutual fund investment account, {}.'.format(format(amount, '.2f'), other.first_name))

						y_n1 = input('\n\n    Are you done investing for today?\n\n(yes/no): ')

						while y_n1 not in ['yes', 'y', 'no', 'n']:
							y_n1 = input('\n\n    Are you done investing for today?\n\n(yes/no): ')

						if y_n1 in ['yes', 'y']:
							done = True

						else:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass



					
				elif choice == '2':
					
					return_rate = r.normalvariate(1.08, 0.05)

					y_n = input('\n\n    Our precious metal & gem fund is really benefitting from the recent discoveries. Fund managers predict that there is a 1 in 3 chance of earning at 10% on your investment annually.\n\n    Want to invest in this? (yes/no): ')
					
					while y_n not in ['yes', 'y', 'no', 'n']:						
						y_n = input('\n\nInvest? (yes/no): ')

					if y_n in ['no', 'n']:						
						y_n = input('\n\n    Still considering the other investment options? (yes/no): ')
						
						while y_n not in ['yes', 'y', 'no', 'n']:							
							y_n = input('\n\nConsidering other investment options? (yes/no): ')

						if y_n in ['yes', 'y']:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass

						else:
							
							done = True

					elif y_n in ['yes', 'y']:
						
						print('\n    You won\'t regret this.')

						amount = input('\n\n    How much would you like to invest in the fund, {}? The least we\'ll invest is $500.\n\nAmount: $'.format(other.first_name))
						done1 = False
						while not done1:
							try:
								
								amount = float(amount)
								
								if 500 <= amount <= other.balance:
									done1 = True
								
								else:
									amount = input('\nInvestment must be at least $500, but no more than your account balance.\n\nAmount: $')
							except:
								amount = input('\nEnter a valid amount over $500 to invest.\n\nAmount: $')

						other.balance -= amount
						other.metal_gem_fund_acct_balance += amount

						print('\n\n    I\'ve deposited {} to your precious metal & gem fund investment account, {}.'.format(format(amount, '.2f'), other.first_name))

						y_n1 = input('\n\n    Are you done investing for today? (yes/no): ')

						while y_n1 not in ['yes', 'y', 'no', 'n']:
							y_n1 = input('\n\n    Are you done investing for today? (yes/no): ')

						if y_n1 in ['yes', 'y']:
							done = True

						else:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass


					
				elif choice == '3':
					return_rate = r.normalvariate(1.14, 0.12)
					

					y_n = input('\n\n    You\'ve probably seen the news lately. These cryptocurrencies are so unpredictable! Still, experts within the company predict you have about an 88% chance of breaking even, and a 47% chance of earning at least 15% annually.\n\n    Want to invest in this? (yes/no): ')
					
					while y_n not in ['yes', 'y', 'no', 'n']:						
						y_n = input('\n\nInvest? (yes/no): ')

					if y_n in ['no', 'n']:						
						y_n = input('\n\n    Still considering the other investment options? (yes/no): ')
						
						while y_n not in ['yes', 'y', 'no', 'n']:							
							y_n = input('\n\nConsidering other investment options? (yes/no): ')


						if y_n in ['yes', 'y']:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass

						else:
							
							done = True

					elif y_n in ['yes', 'y']:
						
						print('\n    Rolling the dice, huh? Hopefully it pays off for you, {}.'.format(other.first_name))

						amount = input('\n\n    How much would you like to invest in the fund? The least we\'ll invest is $500.\n\nAmount: $')
						done1 = False
						while not done1:
							try:
								
								amount = float(amount)
								
								if 500 <= amount <= other.balance:
									done1 = True
								
								else:
									amount = input('\nInvestment must be at least $500, but no more than your account balance.\n\nAmount: $')
							except:
								amount = input('\nEnter a valid amount over $500 to invest.\n\nAmount: $')

						other.balance -= amount
						other.crypto_acct_balance += amount

						print('\n\n    I\'ve deposited {} to your cryptocurrency investment account, {}.'.format(format(amount, '.2f'), other.first_name))

						y_n1 = input('\n\n    Are you done investing for today? (yes/no): ')

						while y_n1 not in ['yes', 'y', 'no', 'n']:
							y_n1 = input('\n\n    Are you done investing for today? (yes/no): ')

						if y_n1 in ['yes', 'y']:
							done = True

						else:
							choice = input('\n\nEnter (1) to learn about our mutual fund.\n\nEnter (2) to learn about our precious metal & gem fund.\n\nEnter (3) to learn about our cryptocurrency options.\n\nEnter (4) if you are done for today.\n\nEntry: ')
							pass


				elif choice == '4':
					print('\n    Okay, {}. Well, feel free to come back if you want to talk more investing.'.format(other.first_name))
					done = True



	def GiveAdvice(self, other):
		print('\n    Hello, {}. I am your advisor {} {}.'.format(other.first_name, self.first_name, self.last_name))
		entry = input('\n\n     I am here to advise you on your financial options and goals. What would you like to discuss today?\n\nEnter (1) to discuss a loan.\n\nEnter (2) to open or add to an investment account.\n\nEnter (3) to check your investment portfolio\'s performance.\n\nEnter (4) to say goodbye\n\nEntry: ')

		done = False
		while not done:
			if entry == '1':
				self.__offer_loan(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				
				while y_n not in ['yes', 'y', 'no', 'n']:
					y_n = input('\n    Will that be all for today? (yes/no): ')

				if y_n.lower() in ['yes', 'y']:
					print('\n    Nice seeing you today, {}.'.format(other.first_name))
					done = True
				elif y_n.lower() in ['no', 'n']:
					entry = input('\n\nEnter (1) to discuss a loan.\n\nEnter (2) to open an investment account.\n\nEnter (3) to check your investment portfolio.\n\nEnter (4) to say goodbye\n\nEntry: ')
				
			elif entry == '2':
				self.__open_investment_account(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				
				while y_n not in ['yes', 'y', 'no', 'n']:
					y_n = input('\n    Will that be all for today? (yes/no): ')

				if y_n.lower() in ['yes', 'y']:
					print('\n    Nice seeing you today, {}.'.format(other.first_name))
					done = True
				elif y_n.lower() in ['no', 'n']:
					entry = input('\nEnter (1) to discuss a loan.\nEnter (2) to open an investment account.\nEnter (3) to check your investment portfolio.\n\nEnter (4) to say goodbye\n\nEntry: ')

			elif entry == '3':

				if other.mutual_fund_acct_balance == 0 and other.metal_gem_fund_acct_balance == 0 and other.crypto_acct_balance == 0:
					print('\n\n    You haven\'t invested with us, yet!\n')
					entry = input('\n\nEnter (1) to discuss a loan.\n\nEnter (2) to open an investment account.\n\nEnter (3) to check your investment portfolio.\n\nEnter (4) to say goodbye\n\nEntry: ')

				else:

					if other.mutual_fund_acct_balance > 0:
						other._customer__mfAccountStatus()

					if other.metal_gem_fund_acct_balance > 0:
						other._customer__mgfAccountStatus()

					if other.crypto_acct_balance > 0:
						other._customer__cryptoAccountStatus()

					y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				
				while y_n not in ['yes', 'y', 'no', 'n']:
					y_n = input('\n    Will that be all for today? (yes/no): ')

				if y_n.lower() in ['yes', 'y']:
					print('\n    Nice seeing you today, {}.'.format(other.first_name))
					done = True
				elif y_n.lower() in ['no', 'n']:
					entry = input('\n\nEnter (1) to discuss a loan.\n\nEnter (2) to open an investment account.\n\nEnter (3) to check your investment portfolio.\n\nEnter (4) to say goodbye\n\nEntry: ')

			elif entry == '4':
				print('\n\n    Goodbye!')
				done = True
				
			else:
				entry = input('\n\nEnter (1) to discuss a loan.\n\nEnter (2) to open an investment account.\n\nEnter (3) to check your investment portfolio.\n\nEnter (4) to say goodbye\n\nEntry: ')


	def talk(self):
		print("Hello! I'm {} {}. I am a Financial Advisor at I.L.L. & Sons.".format(self.first_name, self.last_name))
