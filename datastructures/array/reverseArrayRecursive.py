#http://www.geeksforgeeks.org/write-a-program-to-reverse-an-array/
import sys 

def reverseArray(array, front,rear):

	if front >= rear:
		return 
	
	temp = array[front]
	array[front] = array[rear]
	array[rear] = temp
	reverseArray(array,front+1, rear-1)





if __name__ == "__main__":
	
	array = raw_input("Enter Array elements, separated by space >> ")	
	array = map(int,array.split())

	front = 0
	rear = len(array) - 1
	
	if not len(array) == 1 or len(array) :
		reverseArray(array,front,rear)

	print "Reversed array is",array
