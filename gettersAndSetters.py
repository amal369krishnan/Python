class Example:
	def __init__(self,fname,lname):
		self.firstName = fname
		self.lastName = lname;

	""" @property is denoting the method as getter

		And this annotation is mentioned which means while calling this function there is no need to specify paranthesis '()' 
		eg:'ex.fullName' insteaded of 'ex.fullName()'
	""" 
	@property
	def fullName(self):
		return self.firstName + self.lastName

	""" setter function for fullname function """
	@fullName.setter
	def fullName(self,name):
		self.firstName, self.lastName= name.split(" ")

	@fullName.deleter
	def delFullName(self):
		print("deleted")
		self.firstName = None
		self.lastName = None

ex = Example("Amal", "Krishnan")
ex.fullName = "Amal Krishnan"
print(ex.fullName)
del ex.delFullName