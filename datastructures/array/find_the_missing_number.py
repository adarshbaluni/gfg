# Problem Statement: http://www.geeksforgeeks.org/find-the-missing-number/
#Name: Adarsh Baluni
# 08/31/2015 12:01 Los Angeles, CA 


def findMissingNumber(array):
	
	size = len(array)+1
	
	totalSum = size * (size + 1) / 2
	
	observedSum = 0
	
	for element in array:
		observedSum = observedSum + element

	return totalSum - observedSum


def xorMethod(array):
	
	x1 = 1
	x2 = 0

	for element in range(2,len(array)+2):
		x1 = x1 ^ element

	for element in array:
		x2 = x2 ^ element

	return x1 ^ x2






if __name__ == "__main__":
	
	array = raw_input("\nEnter Array elements , separated by space >> ")
	
	array = map(int,array.split())

	
	choice = raw_input("\n You can find the number by using:\
	 \n 1. Sum of elements method \n\t OR \n 2. XOR method. \n Choose one... >> ")
	
	if choice == 1:
			result = findMissingNumber(array)
	else:
			result = xorMethod(array)
	
	print '\nThe missing number is  %r' % result 
