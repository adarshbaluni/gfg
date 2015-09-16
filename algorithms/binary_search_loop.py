# Find the problem statement here http://geeksquiz.com/binary-search/
#Name: Adarsh Baluni




def binary_search():
	array = [99,13,56,72,8,3,-23,5,-235]
	
	array.sort()    # in-place sorting
	print "The list of numbers is : ", array
	key = input(">> Enter the number you want to search ")
	left = 0
	right = len(array) - 1

	while 1:
		mid = (left + right) / 2
		
		if(array[mid] == key):

			return 1

		elif(left > right ):
			return -1

		else:
			if(key > array[mid]):
				left = mid + 1

			else:
				right = mid - 1





if __name__ == "__main__":
	result = binary_search()
	if(result == 1):
		print "Number found in the list" 
	else:
		print "Not found!"


