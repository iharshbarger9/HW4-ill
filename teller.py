from employee import *

class teller(employee):
	def __init__(self):
		employee.__init__(self)
		
	def ServeCustomer(self, other):
		print('\n\n    Hello there, {}! Hope you are doing well!\n\n    How can I help you today?'.format(other.first_name))
		
		done = False
		while not done:
			choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal  \n\nEnter (4) to make a payment on your outstanding balance \n\nEnter (5) to say goodbye\n\nEntry: ')
			if choice == '1':
				other._customer__check_balance()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '2':
				other._customer__deposit()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '3':
				other._customer__withdrawal()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '4':
				print('\n\n    Your current outstanding balance is ${}.'.format(format(other.outstanding_balance, '.2f')))
			elif choice == '5':
				print('\nGoodbye!')
				done = True
			else:
				choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal  \n\n  Enter (4) to make a payment on your outstanding balance \n\nEnter (5) to say goodbye. \n\nEntry: ')
			print('\nHave a nice day!')

	def talk(self):
		print("Hello! I'm {} {}. I am a teller at I.L.L. & sons.".format(self.first_name, self.last_name))
