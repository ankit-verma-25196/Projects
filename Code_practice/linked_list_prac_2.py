# Linked List Implementation

class Node:
	data = -1
	next = None

	def __init__(self,data):
		self.data = data

def display_LL(head):
	if head == None:
		return None

	temp = head
	while temp != None:
		print(temp.data,end="->")
		temp = temp.next

def insert_at_head(head,data):
	if head == None:
		return Node(data)

	new_node = Node(data)
	new_node.next = head
	head = new_node
	return head


def sum_LL_same_size(head1, head2):
	if head1 == None or head2 == None:
		print("\nhead1="+str(head1))
		print("head2="+str(head2))
		return (None,0)

	result = Node(0)
	returned_node,carry = sum_LL_same_size(head1.next, head2.next)
	
	print("\nReturning from Recursion")
	print()
	print(returned_node)
	print(carry)
	print()
	result.next = returned_node
	sum_ = head1.data + head2.data
	carry = sum_//10
	result.data = sum_ %10
	return(result,carry)

def sum_LL(head1, head2):
	result,carry = sum_LL_same_size(head1, head2)
	if carry == 0:
		return result
	n = Node(carry)
	n.next = result
	return n

head1 = None
n = int(input())
while n>0:
	d = int(input())
	head1 = insert_at_head(head1,d)
	n-=1

display_LL(head1)

print()

head2 = None
n = int(input())
while n>0:
	d = int(input())
	head2 = insert_at_head(head2,d)
	n-=1

display_LL(head2)

sum_ = sum_LL(head1,head2)

display_LL(head1)
print()
display_LL(head2)
print()
display_LL(sum_)




