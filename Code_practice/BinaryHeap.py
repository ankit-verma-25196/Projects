# Implementation of Binary Heap

# max heap
def upheapify(heap, idx):
	if idx == 0:
		return

	pi = (idx-1)// 2 # index of parent -> parent index
	if heap[pi] < heap[idx]:
		# do swapping
		temp = heap[pi]
		heap[pi] = heap[idx]
		heap[idx] = temp
		upheapify(heap, pi)

	else:
		# parent is correct
		return


def downheapify(heap, idx):
	lc = 2*idx + 1 # left child index
	rc = 2*idx + 2 # right child index
	
	if lc >= len(heap) and rc >= len(heap):
		# This means we are on the heap, jus return
		return

	largest = idx
	if lc < len(heap) and heap[lc] > heap[largest]:
		largest = lc

	if rc < len(heap) and heap[rc] > heap[largest]: # rc < len(heap) - This is kept when only lc is there AND no rc is there
		largest = rc

	if largest == idx:
		# no need to down heapify, we are at right place, just return
		return
	temp = heap[largest]
	heap[largest] = heap[idx]
	heap[idx] = temp
	downheapify(heap, largest)

def insert(heap, key):
	heap.append(key)
	upheapify(heap, len(heap)-1)


def get(heap):
	# return highest priority element
	return heap[0]

def removepeek(heap):
	i = len(heap) - 1
	temp = heap[0]
	heap[0] = heap[i]
	heap[i] = temp
	heap.pop()
	downheapify(heap, 0)

def buildheap(heap):
	i = len(heap) - 1
	i = (i // 2) + 1
	while i >= 0:
		downheapify(heap, i)
		i -= 1
	return

# In python , list is passed by reference

heap =[int(x) for x in input().split()]
buildheap(heap)
print(heap)

'''
input:
45 32 67 89 12 -1 5 7 44
output:
[89, 45, 67, 44, 12, -1, 5, 7, 32]
'''

'''
heap = []
n = int(input())
while n > 0:
	n -= 1
	x = int(input())
	insert(heap, x)

print(heap)
'''

'''
input
9
45
32
67
89
12
-1
5
7
44

output
[89, 67, 45, 44, 12, -1, 5, 7, 32]

'''



																												

