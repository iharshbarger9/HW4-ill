from person import person
from person import make_routingNumber
from person import make_ssn
import random as r
from datetime import datetime as dt

class employee(person):

	def __init__(self):
		person.__init__(self)
		self.employee_permissions = True

	def ShowCustomerInfo(self, other):
		print( 'Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, str(other.account_number).zfill(12), other.routing_number, other.balance))
			
	def DeleteCustomer(self, other):
		print('\nAction denied. Must be a manager to perform this action.')

	def SeeCustomers(self):
		print('\nNumber of customers: {}'.format(len(person.customer_list)))




