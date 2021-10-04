# sort the 2 sorted lists and merge into one

def merge(arr1, arr2):
	l1 = len(arr1)
	l2 = len(arr2)

	i = 0
	j = 0
	final = [0]*(l1+l2)
	print("l1 =",arr1)
	print("l2 =",arr2)
	k = 0
	while i<l1 and j<l2:
		if arr1[i]<=arr2[j]:
			final[k]=arr1[i]
			k+=1
			i+=1
		else:
			final[k]=arr2[j]
			k+=1
			j+=1

	while i<l1:
		# If arr1 is remaining and arr2 is exhausted
		final[k]=arr1[i]
		k+=1
		i+=1

	while j<l2:
		# If arr2 is remaining and arr1 is exhausted
		final[k]=arr2[j]
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

arr = [5,4,3,2,1]
left = 0
right = len(arr)-1
output = merge_sort(arr,left,right)
print(output)

'''	
arr1 = [1,3,6,7,10]
arr2 = [2,4,5,8,9]

final = merge(arr1,arr2)
print("final merged = ",final)
'''
