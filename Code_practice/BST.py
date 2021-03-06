# Binary Search Tree

class Node:
	data = -1
	left = None
	right = None

	def __init__(self, data):
		self.data = data

def insertElement(root, data):
	if root == None:
		return Node(data)

	if data < root.data:
		root.left = insertElement(root.left, data)
	else:
		root.right = insertElement(root.right, data)

	return root

def remove(root, key):# key is to be deleted
	if root == None:
		return root
	
	#search for the key
	if key < root.data:
		root.left = remove(root.left, key)
		return root
	elif key > root.data:
		root.right = remove(root.right, key)
		return root
	else:
		if key == root.data:
			# when node is a leaf node - with no left and right child
			if root.left == None and root.right == None:
				# We don't need to delete manually
				# We will return None and now store None instead of child
				return None
			elif root.left != None and root.right == None:
				temp = root.left
				root.left = None
				return temp

			elif root.left == None and root.right != None:
				temp = root.right
				root.left = None
				return temp
			else:
				# When both left and right sub trees exists
				#find next big node
				nextbig = root.right
				while nextbig.left != None:
					nextbig = nextbig.left
				root.data = nextbig.data
				print("nextbig.data = "+str(nextbig.data))

				root.right = remove(root.right, nextbig.data)
				return root
				
 
def preorder(root):
	if root == None:
		return

	print(root.data, end = ", ")
	preorder(root.left)
	preorder(root.right)

def inorder(root):
	if root == None:
		return

	inorder(root.left)
	print(root.data, end = ", ")
	inorder(root.right)

def postorder(root):
	if root == None:
		return

	postorder(root.left)
	postorder(root.right)
	print(root.data, end = ", ")

def buildBSTRec():
	d = int(input())
	root = None
	while d != -1:
		root = insertElement(root, d)
		d = int(input())
	return root

root = buildBSTRec()
print()
preorder(root)
print()
inorder(root)
print()
remove(root, 5)
print()
preorder(root)
print()
inorder(root)
print()

'''
Input
11
5
1
8
20
30
15
31
6
7
10
9
-1
'''
