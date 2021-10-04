# Stack using Arrays
class Stack:
	__arr = [] # private data members using starting with double underscore --> __
	__top = -1
	
	def __init__(self, n):
		self.__arr = [0]*n

	def push(self, element):
		if self.__top > len(self.__arr) - 1:
			print("Overflow Error !!")
			return

		self.__top += 1
		self.__arr[self.__top] = element

	def pop(self):
		if self.__top < 0:
			print("Underflow Error !!")
			return

		temp = self.__arr[self.__top]
		self.__top -= 1
		return temp # return the element which is deleted

	def peek(self):
		if self.__top < 0:
			print("Underflow Error , No Element in stack !!")
			return

		return self.__arr[self.__top]

	
s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.push(40)
s.pop()
s.pop()
print(s.peek())

