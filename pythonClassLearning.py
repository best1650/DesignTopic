# Python Constructor
'''
class Addition:
	value1 = 0
	value2 = 0

	def __init__(self, v1, v2):
		print("Addition Constructor")
		self.value1 = v1
		self.value2 = v2
	
	def getSum(self):
		return self.value1 + self.value2
		
	def __del__(self):
		print("Addition Destructor")

class Person(object):
	def __init__(self, name):
		self.name = name
	
	def getName(self):
		return self.name
	
	def isEmployee(self):
		return False

class Employee(Person):
	def isEmployee(self):
		return True

if __name__ == '__main__':
	addObj = Addition(10, 20)
	print("Answer:%d" % (addObj.getSum()))
	
	p = Person('p1')
	print(p.isEmployee())
	
	e = Employee('e1')
	print(e.isEmployee())

'''


# Check if a class is subclass of another
class Base(object):
	pass

class Derived(Base):
	pass

print(issubclass(Derived, Base))
print(issubclass(Base, Derived))	
	
	
