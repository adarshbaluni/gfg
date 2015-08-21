# Write a Python program that, 
#given an array A[] of n numbers and another number x, 
#determines whether or not there exist two elements in S whose sum is exactly x.

import sys

array=raw_input(">> enter elements of array separated by space >> ")

array=array.split()
array=map(int,array)
array=sorted(array)

x=int(raw_input(">> enter the sum of elements >> "))

rear=len(array)-1
front =0
count=0
pairs=[]

while front < rear:
	if array[front]+array[rear]==x:
		pairs.append([array[front],array[rear]])
		count+=1
		front+=1
		rear-=1
			

	elif array[front]+array[rear]>x:
		rear-=1
	else:
		front+=1

if(count==0):
			print "Pair of elements that Sum up to %d does not exist" % x
else:
	print "There are/is %d such pairs \n " % count
	print pairs
	
	