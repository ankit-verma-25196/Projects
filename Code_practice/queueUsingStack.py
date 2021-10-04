# Implement Queue by Stack
#Push Efficient 

class Queue:
	primary = []
	secondary = []
	cs = -1

	def __init__(self):
		self.cs = 0

	# Push Efficient

	def push(self, data):
		self.primary.append(data)	
		self.cs += 1	

	def pop(self):
		i = self.cs - 1

		while i > 0:
			i -= 1
			self.secondary.append(self.primary[-1])
			self.primary.pop()

		print("Element Removed = ",self.primary[0])
		self.primary.pop()

		while len(self.secondary) > 0:
			x = self.secondary[-1]
			self.primary.append(x)
			self.secondary.pop()

		self.cs -= 1

	def display(self):
		i = self.cs - 1

		while i >= 0:
			i -= 1
			self.secondary.append(self.primary[-1])
			self.primary.pop()

		while len(self.secondary) > 0:
			x = self.secondary[-1]
			print(x)
			self.primary.append(x)
			self.secondary.pop()
		print("###############")

qu = Queue()
qu.push(10)
qu.push(20)
qu.push(30)
qu.push(40)
qu.push(50)
qu.push(60)
qu.push(70)
qu.display()
qu.pop()
qu.pop()
qu.display()



