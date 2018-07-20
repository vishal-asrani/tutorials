from base import *
class  Employee(Person):
	"""docstring for  Employee"""
	def __init__(self, first, last, emp_id):
		super(Employee, self).__init__(first, last)
		self.emp_id = emp_id

	def details(self):
		print(super(Employee, self).name() + " " + self.emp_id)


y = Employee("Vishal", "Dhoni", "64")
y.details()