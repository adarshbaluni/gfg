from collections import deque

class Calculator(object):
	def __init__(self,a,b):
		self.x = a
		self.y = b

	def addition(self):
		return self.x+self.y
	
	def sub(self):
		return self.x-self.y
	
	def mul(self):
		return self.x*self.y
	
	def div(self):
		if(self.y==0):
			print "\n <EXCEPTION> Divide by zero exception\n"
			return False 
		return self.x/self.y


if __name__ == "__main__":

	ip = raw_input(">> ")
	#print "\n --", ip
	exp = list(ip)
	exp = deque(exp)
	for i in xrange(0,len(exp),2):
		exp[i] = int(exp[i])

	i = 1
	value = 0

	while(len(exp) >1):
		if(exp[i] == '+'):
			c = Calculator(exp[0],exp[2])
			value = c.addition()
			

		elif(exp[i] == '-'):
			c = Calculator(exp[0],exp[2])
			value = c.sub()
			

		elif(exp[i] == '*'):
			c = Calculator(exp[0],exp[2])
			value = c.mul()
			

		elif(exp[i] == '/'):
			c = Calculator(exp[0],exp[2])
			value = c.div()
			if value == False:
				#print"\n Invalid.."
				break

		exp.popleft()
		exp.popleft()
		exp.popleft()
		exp.appendleft(value)
		
			


	if value == False:
		print "\n\ninvalid expression due to Divide by zero"
	else:
		print "\n\n value of the expression is : ",exp[0]




