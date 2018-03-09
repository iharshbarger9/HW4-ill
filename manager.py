from employee import *

class manager(employee):

	def __init__(self):
		employee.__init__(self)
		self.manager_permissions = True
    
	def ShowCustomerInfo(self, other):
		print('\nCustomer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nSocial Security Number: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, other._person__ssn, str(other.account_number).zfill(12), other.routing_number, other.balance))

	def SeeCustomers(self):
		for customer in person.customer_list:
			print('\nName: {}      Acct #: {}'.format(customer.name, str(customer.account_number).zfill(12)))

	def DeleteCustomer(self, other):
		done = False
		while not done:
			y_n = input('\nDelete {}? (yes/no): '.format(other.name))
			if y_n.lower() in ['yes', 'y']:
				print('Deleting...')
				person.past_customer_list.append(person.customer_list.pop(other.customer_number))
				done = True
			elif y_n.lower() in ['no', 'n']:
				print('\nNot deleted.')
				done = True

	def SeeDebtsToBank(self):
		total = 0
		count = 0
		for customer_ in person.customer_list:
			if customer_.outstanding_balance > 0:
				count += 1
				total += customer_.outstanding_balance
        
		print('\n\n    ${} is owed to the bank by {} customers.'.format(total, count))

	def talk(self):
		print("Hello! I'm {} {}. I am a manager at I.L.L. & sons.".format(self.first_name, self.last_name))

