# Linked List implementation in python:
# Dynamic Size
# Ease of insertion/deletion of an element

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self,data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialise head
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

# Code Execution
if __name__=='__main__':

	# Starting with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second # Link first node with second

	# next of first Node refers to second

	second.next = third # Link second node with third

	# next of second Node refers to third

	#printing the Linked List
	llist.printList()

