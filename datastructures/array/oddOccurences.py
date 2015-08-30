#Problem Description: http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
#Author: Adarsh Baluni 08/29/2015 19:38 Los Angeles, CA


#####--------------------------------------------------------------------

def getOddOccurences(array):
	result = 0
	for element in array:
		result = result ^ element

	return result




if __name__ == "__main__":
	
	array = raw_input("Enter Array elements , separated by space >> ")
	
	array = map(int,array.split())

	result = getOddOccurences(array)

	print 'The number with od occurances is %r' % result 

	