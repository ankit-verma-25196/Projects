# Linked List Practice

class Node:
	data = -1
	next = None

	def __init__(self,data):
		self.data = data

def insert_at_head(head,data):
	if head == None:
		return Node(data)

	new_node = Node(data) #making new node
	new_node.next = head
	head = new_node
	return head

def insert_at_tail(head,data):
	if head == None:
		return Node(data)

	temp = head
	while temp.next != None:
		temp = temp.next

	new_node = Node(data)
	temp.next = new_node
	return head

def insert_at(head,data,pos=0):
	if pos == 0:
		return insert_at_head(head,data)
	elif pos >= sz_of_LL(head):
		return insert_at_tail(head,data)

	temp = head
	while pos != 1:
		temp = temp.next
		pos -= 1

	new_node = Node(data)
	new_node.next = temp.next
	temp.next = new_node

	return head

def delete_at_head(head):
	if head == None:
		return None

	temp = head
	head = temp.next
	temp.next = None

	return head

def delete_at_tail(head):
	if head == None:
		return None

	# get the element just before tail
	temp = head
	prev =None
	while temp.next != None:
		prev = temp
		temp = temp.next

	prev.next = None
	return head

def delete_at(head,pos=0):
	if pos == 0:
		# delete at head
		return delete_at_head(head)
	elif pos >= sz_of_LL(head):
		return delete_at_tail(head)

	temp = head
	while pos!=1:
		temp = temp.next
		pos -= 1

	tobedeleted = temp.next
	temp.next = temp.next.next
	tobedeleted.next = None
	return head

#Delete using value instead of position - given "head of LL" and "val of node to be deleted"
def delete_using_val(head,val):
	if head == None:
		return None

	temp = head
	prev = None
	while temp.data != val:
		prev = temp
		temp = temp.next

	print(temp.data)

#	tobedeleted = temp
	prev.next = temp.next
	temp.next = None

	return head

def delete_all_same_vals(head,val):
	if head == None:
		return None

	while True:
		if find_element(head,val):
			head = delete_using_val(head,val)
			display_LL(head)
		else:
			break
		
def find_element(head,val):
	if head == None:
		return None

	temp = head
	while temp.next != None:
		if temp.data == val:
			return True
		temp = temp.next

	return False
# Pointer Iterative
def reverse_LL(head):
	if head == None:
		return None

	prev_,curr_,next_ = None,head,head.next
	while next_ != None:
		curr_.next = prev_
		prev_ = curr_
		curr_ = next_
		next_ = next_.next

	#update the last node
	curr_.next = prev_
	return curr_


def sz_of_LL(head):
	sz = 0
	temp = head
	while temp != None:
		sz += 1
		temp = temp.next

	return sz

def display_LL(head):
	temp = head

	while temp != None:
		print(temp.data,end="->")
		temp = temp.next

	print()



n = int(input())
head = None

while n>0:
	data = int(input())
	if n %2 == 0:
		head = insert_at_head(head,data)
	else:
		head = insert_at_tail(head,data)

	display_LL(head)
	n -= 1

display_LL(head)
head = delete_using_val(head,3)
display_LL(head)
print(find_element(head,2))
print(find_element(head,4))
print(find_element(head,3))
delete_all_same_vals(head,9)
head = reverse_LL(head)
display_LL(head)
'''
head = insert_at(head,8,pos=4)
display_LL(head)
head = delete_at_head(head)
display_LL(head)
head = delete_at_tail(head)
display_LL(head)
head = delete_at(head,pos=3)
display_LL(head)
'''
print("size of LL=",sz_of_LL(head))



