#code to find x^y
def xPowery(v,n):
	
	if(n==0):
		return 1
	if(n==1):
		return v
	if(n < 0):
		return 1/v *  xPowery(v,n+1)
	else:
		return int(v * xPowery(v,n-1))


if __name__ == '__main__':
	result = xPowery(float(3),-5)
	print result
