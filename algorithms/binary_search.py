# Find the problem statement here http://geeksquiz.com/binary-search/
#Name: Adarsh Baluni


def binarySearch(array, left, right, key):
	
	mid = (left + right) / 2

	if (right >= left):
		
		if key == array[mid]:
		
			return 1
	
		elif key < array[mid]:
		
			return binarySearch(array, left, mid-1, key)                      #if array is too big,we can have left and right indices passed as values alongwith key . Will be required to make array global
	
		else:
		
			return binarySearch(array, mid+1, right, key)
	
	else:		
			return -1




if __name__ == "__main__":
	
	array = raw_input("Enter Array elements, separated by space >> ")
	
	array = map(int,array.split())

	array.sort()                                            #Sorts the list/array in-place

	print array

	key = input("Enter the element you would like to search >> ") 

	result = binarySearch(array, 0, len(array)-1, key)

	if result == -1 :
		print "The element was not found"
	else:
		print "The element found" 
