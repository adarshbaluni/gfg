#http://geeksquiz.com/bubble-sort/

import sys

def bubbleSort() :

	array = input("Enter array elements (within [] brackets separated by ,) >>" )
	
	for outer in range(0,len(array)):
		swap = 0
	
		for inner in range(0,len(array)-outer-1):
	
			if array[inner] > array[inner + 1]:
				temp = array[inner]
				array[inner] = array[inner + 1]
				array[inner + 1] = temp
				swap = 1

		if swap == 0:
			break 

	print array





if __name__ == '__main__' :
	bubbleSort()