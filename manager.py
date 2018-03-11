from employee import *

class manager(employee):

	def __init__(self):
		employee.__init__(self)


	def ShowCustomerInfo(self, other):
		'''Shows an active customer's personal and account information.'''
		if not other._customer__deleted_customer:
			print('\nCustomer: {}\n\nD.O.B: {}/{}/{}\n\nAddress: {}\n\nSocial Security Number: {}\n\nAccount Number: {}\n\nRoutingNumber: {}\n\nChecking Account Balance: {}\n\nNet Worth: ${}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, other._person__ssn, str(other.account_number).zfill(12), other.routing_number, other.balance, format(other.balance + other.crypto_acct_balance + other.mutual_fund_acct_balance + other.metal_gem_fund_acct_balance, '.2f')))

	def SeeCustomers(self):
		'''Will display the name and checking account number for every person on the active customer list'''
		for customer in person.customer_list:
			print('\n\n{}) Name: {}      Acct #: {}'.format(customer.customer_number + 1, customer.name, str(customer.account_number).zfill(12)))

	def DeleteCustomer(self, other):
		'''Will move a customer from the active customer list to the past customer list. This will disable their customer privileges.'''
		if not other._customer__deleted_customer:
			y_n = input('\n\n    Delete {}? (yes/no): '.format(other.name))
			while y_n.lower() not in ['yes', 'y', 'no', 'n']:
				y_n = input('\n\n    Delete? (yes/no): ')
			if y_n.lower() in ['yes', 'y']:
				print('\nDeleting...')
				person.past_customer_list.append(person.customer_list.pop(other.customer_number))
				other._customer__deleted_customer = True
				print('\n\nDone.')
			else:
				print('\n\nNot deleted.')

	def ReactivateCustomer(self, other):
		'''Reactivates a deleted customer by moving him/her from the past customer list to the active customer list. This renables their customer privileges.'''
		if other._customer__deleted_customer:
			y_n = input('\n\n    Reactivate {}\'s accounts? (yes/no): ')
			while y_n.lower() not in ['yes', 'y', 'no', 'n']:
				y_n = input('\n\n    Reactivate? (yes/no): ')
			if y_n in ['yes', 'y']:
				print('\nReinstating...')
				
				for index in range(len(person.past_customer_list)):
					if person.past_customer_list[index]._person__ssn == other._person__ssn:
						person.customer_list.append(person.past_customer_list.pop(index))
						other._customer__deleted_customer = False

				print('\n\nDone.')

			else:
				print('\n\nNot Reactivated.')

	def SeeDebtsToBank(self):
		'''Will show the total of all the outstanding balances owed to the bank and by how many customers'''
		total = 0
		count = 0
		for customer_ in person.customer_list:
			if customer_.outstanding_balance > 0:
				count += 1
				total += customer_.outstanding_balance
		print('\n\n    ${} is owed to the bank by {} customers.'.format(format(total, '.2f'), count))
    
	def talk(self):
		'''Manager will introduce himself'''
		print("Hello! I'm {} {}. I am a manager at I.L.L. & Sons.".format(self.first_name, self.last_name))