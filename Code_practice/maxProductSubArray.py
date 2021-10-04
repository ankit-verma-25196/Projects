# maximum product sub array
'''
Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -40, 0, -2, -3}
Output:   80  // The subarray is {-2, -40}
'''

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass

	print(l1)

	finalProduct = l1[0]
	prev = l1[0]
	product = l1[0]

	for i in range(1,n):
		if prev < l1[i]:
			product *= l1[i]
		else:
			product = l1[i]

		prev = l1[i]

		finalProduct= max(finalProduct, product)
		print("product = "+str(product))
		print("final product = "+str(finalProduct))
	
	print(finalProduct)

try:
	for tc in range(int(input())):
		solve()
except:
	pass

