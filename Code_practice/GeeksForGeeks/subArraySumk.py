import math
import sys

# continuous sub array with sum=k

def solve():
	NS = list(map(int,input().split()))
	n = NS[0]
	s = NS[1]

	arr = list(map(int,input().split()))

	l = 0	
	r = 0
	sum_ = 0
	ans_arr = []
	res = 0
	
	'''
	pre_sum = [0]*n
	
	for i in range(len(arr)):
		pre_sum[i] = pre_sum[i-1] + arr[i]

	print(pre_sum)
	'''
	while r<n:
		sum_ += arr[r]
#		print("out sum = "+str(sum_))
#		print()
		while l <= r and sum_ > s:
#			print("in sum 1= "+str(sum_))
			sum_ -= arr[l]
#			print("in sum 2= "+str(sum_))
			l += 1
#		print()
		if sum_ == s:
			res += 1
			print(l+1,end= " " )
			print(r+1)
			break
		r += 1

#	print(res)
	


	'''			
	if len(ans_arr)!=0:
		print(ans_arr)
	else:
		print(-1)
	'''

try:
	for tc in range(int(input())):
		solve()
except:
	pass
	
