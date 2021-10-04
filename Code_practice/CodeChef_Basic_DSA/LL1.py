# https://www.codechef.com/UADS1001/problems/LL1

class Node:
	data = -1
	next = None

	def __init__(self, data):
		self.data = data

def insert_at_tail(head, data):
	if head == None:
		return Node(data)

	temp = head

	while temp.next != None:
		temp = temp.next

	new_node = Node(data)
	temp.next = new_node

	return head

def print_LL(head):
	temp = head

	while temp != None:
		print(temp.data, end="-> ")
		temp = temp.next
		
	print()
	return

def size_of_LL(head):
	sz = 0
	temp = head
	while temp != None:
		sz += 1
		temp = temp.next
	return sz

def getNthNodeFromEnd(head, n):
	if head == None:
		return None

	sz = size_of_LL(head)
	print("sz = "+str(sz))

	fromStart = sz - n
	print("fromStart = "+str(fromStart))

	temp = head

	while fromStart != 0:
		temp = temp.next
		fromStart -= 1

	return temp.data


n = int(input())
head = None
while n > 0:
	d = int(input())
	head = insert_at_tail(head, d)
	n -= 1

print_LL(head)
print(getNthNodeFromEnd(head, 1))
