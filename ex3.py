import time

class timer:
	def __init__(self,func):
		self.func = func
		self.alltime = 0
	def __call__(self,*args,**kargs):
		start = time.clock()
		result = self.func(*args,**kargs)
		elapsed = time.clock() - start
		self.alltime += elapsed
		print "%s:runtime:%.5f,alltime:%.5f"%(self.func.__name__,elapsed,self.alltime)
		return result

@timer
def listfunc(N):
	return [x*2 for x in range(N)]
	
@timer
def mapfunc(N):
	return list(map((lambda x:x*2),range(N)))
	
if __name__ == '__main__':
	result1 = listfunc(500000)
	result2 = mapfunc(500000)