# Linked List Practice

class Node:
	data = -1
	next = None

	def __init__(self, data):
		self.data = data


def insert_at_head(head, data):
	if head == None:
		return Node(data)

	new_node = Node(data)
	new_node.next = head
	head = new_node
	return head

def insert_at_tail(head, data):
	if head == None:
		return Node(data)

	temp = head
	while temp.next != None:
		temp = temp.next

	new_node = Node(data)
	temp.next = new_node
	new_node.next = None
	return head

def size_of_LL(head):
	temp = head
	sz = 0
	while temp != None:
		temp = temp.next
		sz += 1

	return sz

def display_LL(head):
	sz = size_of_LL(head)
	print("The size of Linked List = "+str(sz))
	
	temp = head
	while temp != None:
		print(temp.data, end = "->")
		temp = temp.next
	
	print()
	return	

head1 = None

# insert the first element in Linked List
head1 = insert_at_head(head1,5)
display_LL(head1)
# insert the other elements in Linked List
head1 = insert_at_head(head1,6)
display_LL(head1)
head1 = insert_at_head(head1,7)
display_LL(head1)
head1 = insert_at_head(head1,8)
display_LL(head1)

display_LL(head1)

