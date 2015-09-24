#http://geeksquiz.com/selection-sort/

import sys

def selectionSort() :

	array = input("Enter array elements (within [] brackets separated by ,) >>" )
	
	for i in range(0,len(array)):
		
		for j in range(0,len(array)-1-i):
			
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

	print 'Sorted array ',array


if __name__ == '__main__' :
	selectionSort()