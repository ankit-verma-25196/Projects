# Max Heap Python

from queue import PriorityQueue

class MaxHeapEl(object):
	def __init__(self, x):
		self.x = x

	def __lt__(self, o): # function overriding - we are overriding "less than" function
		return self.x > o.x


	def __str__(self,): # function overriding - we are overriding str function
		return str(self.x)

max_heap = PriorityQueue()
max_heap.put(MaxHeapEl(10))	
max_heap.put(MaxHeapEl(200))
max_heap.put(MaxHeapEl(30))
max_heap.put(MaxHeapEl(40))
max_heap.put(MaxHeapEl(-10))

print(max_heap.get())
print(max_heap.get())
print(max_heap.get())
