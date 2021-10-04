# counting sort

# 1,1,5,4,5,3,4,1,2

# in dictionary - insertion, delete, update, search - done in O(1) 

# different buckets having number that says number of times an element occurs

# TC - O(n + (max - min)) --> O(n+k)

# Stable(Basic Implementation - NOT stable) - No - as relative ordering has changed - only dict based implementation is NOT Stable

# like jenga game

# prefix sum ? last class --> prefix sum for an current element is = sum of elements from starting element to current element

# Analysis
# Stable - YES with using prefix sum (cumulative sum)
# inplace - NO
# Space Complexity - O(n + k)
# Time Compleity - O(n+n+k) - O(n+k)
# swaps - no
# comparison - no

# caveats for counting sort - disadvantages for the counting sort

# what is master theorem


def counting_sort(arr):
	# in this implementation we will assume that we get only positive values
	max_element = max(arr)
	freq = [0]*(max_element+1)
	
	# this loop will help to create the frequency list
	for i in range(0, len(arr)):
		freq[arr[i]] += 1

	# now we need to prepare prefix sum
	for i in range(1, len(freq)):
		freq[i] = freq[i] + freq[i-1]

	# freq[arr[i]] -> the position of the currrent value arr[i]
	# arr[i] -1 -> the index where arr[i] has to be placed
	output = [0]*len(arr)
	for i in range(len(arr)-1, -1 , -1): # going from last element to maintain stability
		output[freq[arr[i]] - 1] = arr[i] #
		freq[arr[i]] -= 1

	return output

li = [1,2,5,0,4,9]	

newli = counting_sort(li)

print(newli)
	
# disadvantage - perform poorly when large number of elements are present
