class Employee:
	raise_percent=1.2;
	count=0
	"""init is same as constructors in other programming languages"""
	"""self is denoting the instance of this class i.e; eg.emp1"""
	def __init__(self, firstName, lastName, salary):
		self.firstName = firstName
		self.lastName = lastName
		self.salary = salary
		Employee.count+=1
	
	"""This is a regular method. so, the first argument must be self(instance)"""
	def fullName(self):
		return '{} {}'.format(self.firstName,self.lastName)

	"""This is a regular method. so, the first argument must be self(instance)"""
	def applyRaise(self):
		# self.salary  = self.salary*Employee.raise_percentself.salary  = self.salary*1.2;
		# self.salary  = self.salary*Employee.raise_percent;
		self.salary  = self.salary*self.raise_percent

	"""This is a class method. so, the first argument must be cls(Class)"""
	@classmethod
	def setRaiseAmount(cls,emp_str):
		name1,name2,name3 = emp_str.split('-')
		return name1+" "+name2+" "+name3

	"""This is a static method. so, no argument is required"""
	@staticmethod
	def isWorking(day):
		if day.weekday()==5 or day.weekday()==6:
			return False;
		return True;


# print(Employee.count)
emp1 = Employee("Amal","Krishnan",15000)
emp2 = Employee("Sasakan","Kumar",12020)
# print(Employee.count)
# print(emp1.fullName())
# print(emp2.fullName())
# emp1.firstName = "Amal"
# emp1.lastName = "Krishnan"
# print(emp1.firstName)
# print(emp2.firstName)

# print(emp1.salary)
# emp1.applyRaise()
# print(emp1.salary)
# print(Employee.__dict__)
# print(emp1.__dict__)

# emp_str = "John-shaper-tesser"
# emp1_str = "groom-bride-child"
# print(Employee.setRaiseAmount(emp1_str))


# import datetime;
# date = datetime.date(2021,9,18)
# print(Employee.isWorking(date))
