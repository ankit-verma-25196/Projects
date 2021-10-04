class ComplexNumber:
	real = 0
	img = 0

	def __init__(self, real ,img): # constructor in python
		self.real = real
		self.img = img

	def display(self):
		print(self.real, f"+ i{self.img}")



c1 = ComplexNumber(5, 3) # this calls the class constructor

c1.display()
