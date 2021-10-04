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


	
def insert_at_head(head, data): # pass by reference
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

def insert_at_tail(head, data):
	if head == None:
		return Node(data)
	temp = head
	while temp.next != None:
		temp = temp.next

	# When above loop ends, temp will be having the Node whose next is None
	new_node = Node(data)
	temp.next = new_node
	return head

def length_of_LL(head):
	temp = head
	sz = 0
	while temp != None:
		sz += 1
		temp = temp.next

	return sz

	
# insert somewhere in the middle

# fetch the node previous to the index where we want to insert
# mark the next of new node= to the node present at the index currently(temp.next)		
# update temp.next = new_node

def insert_at(head, data, pos = 0):
	# calculate the size of linked list because someone can give you position which is bigger than length of the linked list
	# so taking care of those cases

	if pos == 0:
		return insert_at_head(head, data)
	if pos >= length_of_LL(head):
		return insert_at_tail(head, data)

	'''
	temp = head
	i = 0
	while temp.next != None:
		temp = temp.next
		i+=1
		if pos == i:
			break
	'''

	temp = head
	while pos != 1:
		pos -= 1
		temp = temp.next
		
	new_node = Node(data)
	new_node.next = temp.next
	temp.next = new_node
	return head

# delete from head , delete from tail, delete from middle

def delete_at_head(head):
	if head == None:
		return None
	temp = head # temp will be automatically collected by garbage collector
	head = head.next
	temp.next = None
	return head

def delete_at_tail(head):
	#get the element just before the tail
	temp = head
	prev = None
	while temp.next != None:
		prev = temp
		temp = temp.next

	# when this loop ends temp points at the tail prev at the previous element
	prev.next = None
	return head

def delete_at(head, pos = 0):
	if pos == 0:
		return delete_at_head(head)
	if pos >= length_of_LL(head):
		return delete_at_tail(head)

	temp = head
	while pos != 1:
		pos -= 1
		temp = temp.next
	
	tobedeleted = temp.next
	temp.next = temp.next.next
	tobedeleted.next = None
	return head

def find_mid_node(head):
	if head == None:
		return head
	fast, slow = head.next, head
	while fast != None and fast.next!=None:
		fast = fast.next.next
		slow = slow.next

	return slow

# 11 22 33 44 , for this if we want to return mid as 22 not 33 as 2 elements are in race of middle => use fast as head.next

def sum_LL_same_size(head1, head2):
	if head1 == None or head2 == None: # base case
		return (None, 0)

	result = Node(0)
	returned_node, carry = sum_LL_same_size(head1.next, head2.next)
	result.next = returned_node
	sum_ = head1.data + head2.data + carry
	carry = sum_//10
	result.data = sum_ % 10
	return (result, carry) # return tupple

# helper function
def sum_LL(head1, head2):
	result, carry = sum_LL_same_size(head1, head2)
	if carry == 0:
		return result
	n = Node(carry)
	n.next = result
	return n

#left = None # global left pointer
def check_palindrome(left, right):
	if right!= None:
		result = check_palindrome(left, right.next)
		left = result[1]
		if not result[0]:
			return (False, left)
		if left.data != right.data:
			return (False, left)

		left = left.next

	return (True, left)

# helper function
def palindrome(head1, head2):
	result = check_palindrome(head1, head2)
	return result[0]

def merge_sorted_ll(left, right):
	if left == None:
		return right
	if right == None:
		return left

	result = None
	if left.data < right.data:
		result = left
		result.next = merge_sorted_ll(left.next, right)
	else:
		result = right
		result.next = merge_sorted_ll(left, right.next)
	return result


def mergesort(head):
	if head == None or head.next == None:
		return head

	mid = find_mid_node(head)
	left = head
	right = mid.next
	mid.next = None

	left = mergesort(left)
	right = mergesort(right)
	result = merge_sorted_ll(left, right)
	return result

# reverse Pointer Iterative
def reversePI(head):
	if head == None:
		return head

	prev_, curr_, next_ = None, head, head.next
	
	while next_ != None:
		curr_.next = prev_
		prev_ = curr_
		curr_ = next_
		next_ = next_.next

	# update the last node
	curr_.next = prev_
	# change the head
	return curr_

# reverse pointer recursive
def reversePR(head):
	if head == None or head.next == None:
		#base case
		return head
	# recurive intuition
	tail = reversePR(head.next)
	head.next.next = head
	head.next = None
	return tail
	
def fold_helper(left, right):
	if right == None:
		return left

	left = fold_helper(left, right.next)

	if left == None:
		return left

	if left != right and left.next != right:
		temp = left.next
		left.next = right
		right.next = temp
		left = temp
	else:
		# when left and right are equal
		right.next = None
		left = None

	return left
# question given - Fold
def fold(head):
	fold_helper(head, head)
	return head

# 1->2->3->4->5->6
# 2->1->4->3->6->5

def reverse_LL(head, k):
	prev = None
	curr = head
	while k > 0:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
		k -= 1

	return prev
		
def reverse_group_k(head, k):
	ptr = head
	new_head = None
	last_tail = None
	while ptr != None:
		count = 0
		ptr = head
		while count < k and ptr != None:
			ptr = ptr.next
			count += 1
		if count == k:
			# Execute Procedure
			rev_head = reverse_LL(head, k)
			if new_head == None:
				new_head = rev_head
			if last_tail != None:
				last_tail.next = rev_head
			last_tail = head
				
			head = ptr	
		
	if last_tail:
		last_tail.next = head
	return new_head if new_head else head
			
n = int(input())
#m = int(input())
head1 = None
head2 = None
while n > 0:
	n -= 1
	x = int(input())
	head1 = insert_at_tail(head1, x)
#	print(head.data)

'''
while m > 0:
	m -= 1
	x = int(input())
	head2 = insert_at_tail(head2, x)
#	print(head.data)
'''

display_LL(head1)

#display_LL(head2)

#sum_ = sum_LL(head1, head2)
#display_LL(sum_)



#head = insert_at(head, 67,  2)
#display_LL(head)

#mid = find_mid_node(head)
#print(mid.data)
#input()
#head = delete_at_head(head)
#display_LL(head)
#head = delete_at_tail(head)
#display_LL(head)
#head = delete_at(head,3)
#display_LL(head)

#left = head1
#print(palindrome(head1, head1))

#head1 = mergesort(head1)
#display_LL(head1)

#head1 = reversePI(head1)
#display_LL(head1)

#head1 = reversePR(head1)
#display_LL(head1)

#head1 = fold(head1)
#display_LL(head1)

head1 = reverse_group_k(head1, 3)
display_LL(head1)






