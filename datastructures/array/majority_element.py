#Problem Description: http://www.geeksforgeeks.org/majority-element/
#Author: Adarsh Baluni 08/25/2015 18:08 Los Angeles, CA


#####--------------------------------------------------------------------



def find_majority_element(element,array):
	
	count = 0
	
	for i in array:
	
		if i == element :
			count += 1
	
			if count > len(array)/2:
				return element

	return 'NONE'



def check_for_majority_element(array):
	
	majority_index=0                    

	count=0                             

	for index,element in enumerate(array):
	
		if(element==array[majority_index]):
			count += 1

		else:
			count -= 1

		if(count == -1):
			majority_index=index
			count = 0

	
	if(count > 0):
		
		return find_majority_element(array[majority_index],array)
	
	else:
	
		return 'NONE'
	

if __name__ == "__main__":
	
	array=raw_input("Enter Array elements, separated by space >> ")
	
	array=map(int,array.split())

	majority_element= check_for_majority_element(array)
	print "Majority Element ", majority_element