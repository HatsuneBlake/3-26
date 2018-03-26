class tracer(object):
	def __init__(self,func):
		self.calls = 0
		self.func = func
	def __call__(self,*args,**kargs):	#self get instance in __get__.wrapper;
										#which means tracer(instance,*args,**kargs);
										#In this example means tracer(bob,.2)
		print 2
		self.calls += 1
		print 'Call %s times to %s'%(self.calls,self.func.__name__)
		return self.func(*args,**kargs) #self is Person instance
	def __get__(self,instance,owner):			 #instance is the Person instance
		print 1
		def wrapper(*args,**kargs):
			return self(instance,*args,**kargs)  #self is a decorator instance,instance is the Person instance
		return wrapper


class Person:
	def __init__(self,name,pay):
		self.name = name
		self.pay = pay
	
	@tracer
	def giveRaise(self,percent):
		self.pay *= (1+percent)
		
		
		
if __name__ == '__main__':
	bob = Person('Bob',20000)
	bob.giveRaise(.2)   #trigger trace.__get__ first
	print bob.pay