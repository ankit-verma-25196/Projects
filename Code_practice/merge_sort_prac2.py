# Merge sort practice - 2

def merge(a,b):
	n = len(a)
	m = len(b)

	i,j,k = 0,0,0
	final = [0]*(n+m)

	while i<n and j<m:
		if a[i]<=b[j]:
			final[k]=a[i]
			k+=1
			i+=1

		else:
			final[k]=b[j]
			k+=1
			j+=1

	while i<n:
		final[k]=a[i]
		k+=1
		i+=1

	while j<m:
		final[k]=b[j]
		k+=1
		j+=1

	return final

def merge_sort(arr,left,right):
	if left==right:
		#base case
		return [arr[left]]
	mid = (left+right)//2

	left_half = merge_sort(arr,left,mid)
	right_half = merge_sort(arr,mid+1,right)

	output = merge(left_half,right_half)
	return output

#arr = [int(x) for x in input().split()]
arr = [9,8,7,6,5,4,3,2,1]
print(arr)
output = merge_sort(arr,0,len(arr)-1)
print(output)


