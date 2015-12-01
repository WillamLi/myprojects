class Person:
    def __init__(self,name,age):
	self.name=name
	self.age=age

    def eat(self):
	print 'I eat'+self.age+'years'
    
    def speak(self):
	print 'my name is'+self.name
a=Person('wd','22')
a.eat()
a.speak()
