# binary search - question2 - given a number , find it's square root
# Time Complexity - O(log n)
# SC - O(1)

def sqrt(x):
	if x == 0 or x == 1:
		return x

	lo, hi, ans = 0, x, x

	while lo <= hi:
		mid = lo + (hi - lo) // 2
		if mid * mid == x:
			return mid
		if mid * mid < x:
			# discard the left half
			lo = mid + 1
			ans = mid # to extend the solution to get the floor value of square root of x
		else:
			hi = mid - 1

	return ans

n = int(input())
print(sqrt(n))
