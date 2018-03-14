from person import person
from customer import make_routingNumber
from person import make_ssn
import random as r
from datetime import datetime as dt

class employee(person):

	def __init__(self):
		person.__init__(self)

	def ShowCustomerInfo(self, other):
		'''Prints a customer's personal and account information, but not their SSN.'''

		if not other._customer__deleted_customer:
			print( 'Customer: {}\n\nD.O.B: {}/{}/{}\n\nAddress: {}\n\nAccount Number: {}\n\nRoutingNumber: {}\n\nChecking Account Balance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, str(other.account_number).zfill(12), other.routing_number, other.balance))

		else:
			print('\n\n    This customer is not active.')
			
	def DeleteCustomer(self, other):
		'''Only managers can change a customer's status as active.'''
		print('\nAction denied. Must be a manager to perform this action.')

	def SeeCustomers(self):
		'''For non-manager employees, this displays the number of customers the bank has.'''
		print('\nNumber of customers: {}'.format(len(person.customer_list)))

	def talk(self):
		'''An employee object is unable to help a customer, so they introduce themselves as just starting out.'''
		print('Hi there! I\'m {} {} and I\'m new here. You could probably ask a manager, advisor, or teller if you need some help.'.format(self.first_name, self.last_name))