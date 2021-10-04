# Binary Tree Implementation

class Node:
	data = -1
	left = None
	right = None

	def __init__(self,data):
		self.data = data


def buildBTRec():
	d = int(input())
	if d == -1:
		return None


	root = Node(d)
	root.left = buildBTRec()
	root.right = buildBTRec()
	return root

def preorder(root):
	if root == None:
		return

	print(root.data,end=", ")
	preorder(root.left)
	preorder(root.right)

def inorder(root):
	if root == None:
		return

	inorder(root.left)
	print(root.data,end=", ")
	inorder(root.right)

def postorder(root):
	if root==None:
		return

	postorder(root.left)
	postorder(root.right)
	print(root.data,end=", ")


root = buildBTRec()
print()
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()



	


