# Linked list node 
class Node:
  
    def __init__(self):
        self.data = None
        self.next = None
  
head = None
  
# Function that returns the largest element 
# from the linked list. 
def largestElement(head): 
  
    # Declare a max variable and initialize 
    # it with INT_MIN value. 
    # INT_MIN is integer type and its value 
    # is -32767 or less. 
    max = -32767
  
    # Check loop while head not equal to None 
    while (head != None):
      
        # If max is less then head.data then 
        # assign value of head.data to max 
        # otherwise node point to next node. 
        if (max < head.data) :
            max = head.data 
        head = head.next
      
    return max
  
# Function that returns smallest element 
# from the linked list. 
def smallestElement(head): 
  
    # Declare a min variable and initialize 
    # it with INT_MAX value. 
    # INT_MAX is integer type and its value 
    # is 32767 or greater. 
    min = 32767
  
    # Check loop while head not equal to None 
    while (head != None) :
      
        # If min is greater then head.data then 
        # assign value of head.data to min 
        # otherwise node point to next node. 
        if (min > head.data) :
            min = head.data 
        head = head.next
      
    return min
  
# Function that push the element in linked list. 
def push( data) :
  
    global head
  
    # Allocate dynamic memory for newNode. 
    newNode = Node() 
  
    # Assign the data into newNode. 
    newNode.data = data 
  
    # newNode.next assign the address of 
    # head node. 
    newNode.next = (head) 
  
    # newNode become the headNode. 
    (head) = newNode 
  
# Display linked list. 
def printList( head) :
  
    while (head != None) :
        print(head.data ,end= " -> ") 
        head = head.next
      
    print("None") 
  
# Driver code
  
# Start with empty list 
# head = new Node() 
  
# Using push() function to construct 
# singly linked list 
# 17.22.13.14.15 
push( 15) 
push( 14) 
push( 13) 
push( 22) 
push( 17) 
print("Linked list is : ") 
  
# Call printList() function to 
# display the linked list. 
printList(head) 
print("Maximum element in linked list: ",end="") 
  
# Call largestElement() function to get 
# largest element in linked list. 
print(largestElement(head)) 
print("Minimum element in linked list: ",end="") 
  
# Call smallestElement() function to get 
# smallest element in linked list. 
print(smallestElement(head),end="") 