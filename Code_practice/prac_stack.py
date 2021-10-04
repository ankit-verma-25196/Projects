# Stack using Arrays
class Stack:
	arr = []
	top = -1
	
	def __init__(self, n):
		self.arr = [0]*n

	def push(self, element):
		if self.top > len(self.arr) - 1:
			print("Overflow Error !!")
			return

		self.top += 1
		self.arr[self.top] = element

	def pop(self):
		if self.top < 0:
			print("Underflow Error !!")
			return

		temp = self.arr[self.top]
		self.top -= 1
		return temp # return the element which is deleted

	def peek(self):
		if self.top < 0:
			print("Underflow Error , No Element in stack !!")
			return

		return self.arr[self.top]

	
s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.push(40)
s.pop()
s.pop()
print(s.peek())
