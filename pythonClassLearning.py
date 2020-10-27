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


# Single Inheritance
class Parent:
    p_v = 10

    def func1(self):
        print(self.p_v)
        print("parent class")

class Child(Parent):
    def func2(self):
        self.p_v = 20
        print(self.p_v)
        print("child class")

obj = Child()
obj.func1()
obj.func2()
obj.func1()


# Multiple Inheritance
class Mother:
    motherName = ''

class Father:
    fatherName = ''

class Son(Mother, Father):
    def __init__(self, mn, fn):
        self.fatherName = fn
        self.motherName = mn

    def parents(self):
        print(self.motherName)
        print(self.fatherName)

son = Son('mon', 'dad')
son.parents()

# Multilevel Inheritance
class Grandfather:
    def __init__(self, gfname):
        self.grandfatherName = gfname

class Father(Grandfather):
    def __init__(self, fname, gfName):
        self.fatherName = fname
        Grandfather.__init__(self, gfName)

class Son(Father):
    def __init__(self, name, fName, gfName):
        self.sonName = name
        Father.__init__(self, fName, gfName)

son = Son('son', 'father', 'grandfather')
print(son.sonName)
print(son.fatherName)
print(son.grandfatherName)

# Encapsulation
class Base:
    def __init__(self):
        self.public = 'public'
        self._protected = '_protected'
        self.__private = '__private'

class Derived(Base):
    def __init__(self):
        Base.__init__(self)

    def test1(self):
        print(self.public)
        print(self._protected)

    def test2(self):
        self._protected = 'hi'

# Polymorphism
class China():
    def capital(self):
        print('Beijing')
    def language(self):
        print('Chinese')

class US():
    def capital(self):
        print('Washington, D.C.')
    def language(self):
        print('English')

c1 = China()
c2 = US()
for country in [c1, c2]:
    country.capital()
    country.language()

def countryTest(country):
    country.capital()
    country.language()

countryTest(c1)
countryTest(c2)

class Animal():
    def type(self):
        print('Animal')

    def name(self):
        print('Animal')

class Dog(Animal):
    def name(self):
        print('Dog')

class Cat(Animal):
    def name(self):
        print('Cat')

obj1 = Dog()
obj2 = Cat()
obj1.type()
obj2.type()
obj1.name()
obj2.name()


# Static Variables
class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable

a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
CSStudent.stream = 'cis'
print(a.stream)  # prints "cis"
print(b.stream)  # prints "cis"



































