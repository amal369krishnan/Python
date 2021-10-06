from classes import Employee

class Student(Employee):
	raise_percent = 3.5
	def __init__(self,fname,last,salary,age):
		super().__init__(fname,last,salary)
		self.age = age


emp1 = Student('Amal','Krishnan',15000,27)
# emp1.applyRaise()
print(emp1.salary)
print(emp1.age)
# print(help(Employee))