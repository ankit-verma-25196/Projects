# insertion sort

def insertion_sort(arr):
	for i in range(1,len(arr)):
		key = arr[i] # this element will be inserted to its correct position
		j = i-1
		while j>=0 and key<arr[j]:
			arr[j+1] = arr[j]
			j-=1

		arr[j+1] = key
		print(arr)

	return arr

li = [int(x) for x in input().split()]
print(insertion_sort(li))
