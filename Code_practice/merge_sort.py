# Merge Sort - comparison based sort

# Comparison based sorts - bubble , selection , insertion 

# First solve this problem
# Given two sorted lists of size n and m , Merge these 2 sorted lists into one new sorted list  and return the final list

#[1,5,7,9] [2,3,10] ---> [1,2,3,5,7,9,10]
# n size     m size ---> n+m size

# in a list , removal is expensive - remove() - removal from first element in WORST CASE is O(n) - don't try to remove

def merge(a,b):
	# Space : O(n + m)
	# time : O(n + m)
	n = len(a) # lenght of first list
	m = len(b) # lenght of second list
	output = [0]*(n+m) # final output list which will be returned
	
	i, j, k = 0, 0, 0
	
	while i < n and j < m:
		if a[i] < b[j]: # stable with if a[i] <= b[j]:
			output[k] = a[i]
			i += 1
			k += 1
		else:
			output[k] = b[j]
			j += 1
			k += 1

	while j < m:
		# list B is remaining and A is finished/exhausted
		output[k] = b[j]
		j += 1
		k += 1

	while i < n:
		# list A is remaining and B is finished/exhausted
		output[k] = a[i]
		i += 1
		k += 1

	return output

def merge_sort(arr, left, right):
	if left == right:
		#base case
		return [arr[left]] # or return [arr[right]]

	mid = (left + right)/2
	left_half = merge_sort(arr, left, mid) # recursively we extracted the left sorted half
	right_half = merge_sort(arr, mid+1, right) # recursively we extracted the right sorted half
	output = merge(left_half, right_half) # merge both the halves
	return output

#li = [5,4,1,7,6,3,0,2]
li = [9,8,7,6,5,4,3,2,1]

output = merge_sort(li, 0 ,len(li)-1)

print(output)

# T(n) is a function which calculates no. of operations to apply merge
# T(n) = 2 T(n/2) + O(n)  ----> Recurrence Relation

# Time Complexity - O(n logn)
# Space Complexity -
#  -- output list will be created how many times
# python/java/ruby - concept of garbage collector - remove everything which is no more required from the memory
# how many single size lists - n
# how many double size  lists - n/2 -->(O(n))...... Here space complexity will be O(n)


# Garbage Collector has the algorithm called - Mark and Sweep

# Depth of Recursion Call Stack  - O(log n)
# Total Space Complexity = O(n +log n) --> which is O(n)

# InPlace - No
# Swaps Involved - Not any
# Stable - Yes
# Home work - No. of comparisons =min(n,m) where n is length of list1 and m = length of list2
# then O(nlog n)

# This is Divide and Conquer type of Algorithm
# 4 paradigms of algorithms - brute force(recursion Based backtracking and everything) , divide and conquer, greedy algo - local optima based algo's, dynamic pro.

