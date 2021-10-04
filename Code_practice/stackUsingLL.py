# stack using Linked Lists

class Node:
	data = -1
	next = None

	def __init__(self, data):
		self.data = data

def display_LL(head):
	temp = head
	while temp != None:
		print(temp.data, end = "->")	
		temp = temp.next

	print()
	return


	
def push(head, data): # pass by reference
	if head == None: # first element
#		head = Node(data)
#		return
		return Node(data)

	new_node = Node(data) # else not first element
	new_node.next = head
	head = new_node
#	return
	return head

# to insert at tail, we need to find the tail
# property of tail node --> next address as None



def pop(head):
	if head == None:
		return None
	temp = head # temp will be automatically collected by garbage collector
	head = head.next
	temp.next = None
	return head


n = int(input())
#m = int(input())
head1 = None
while n > 0:
	n -= 1
	x = int(input())
	head1 = push(head1, x)
#	print(head.data)



