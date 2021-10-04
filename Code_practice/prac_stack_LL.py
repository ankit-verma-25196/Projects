# Implement Stack using Linked lists

class Stack:
	data = -1
	next = None

	def __init__(self, data):	
		self.data = data

def display_LL(head):
	if head == None:
		 print("None")

	temp = head
	while temp != None:
		print(temp.data, end="->")
		temp = temp.next

	print()
	return

def push(head, data): # Add the element into the list
	if head == None:
		return Stack(data)

	new_node = Stack(data)
	new_node.next = head
	head = new_node
	return head

def pop(head): # Delete the element from Linked List from head
	if head == None:
		return None # return None when there is no element to be deleted

	temp = head
	head = head.next
	temp.next = None
	return head


n = int(input())

head1 = None

while n > 0:
	n -= 1
	x = int(input())
	head1 = push(head1, x)
display_LL(head1)
head1 = pop(head1)
display_LL(head1)

	
	
