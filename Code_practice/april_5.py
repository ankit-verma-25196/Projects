import sys
import math

def solve():
	try:
		nmk = list(map(int, input().split()))
		n = nmk[0]
		m = nmk[1]
		k_st = nmk[2]
		arr = []
		for i in range(n):
			col = list(map(int, input().split()))
			arr.append(col)

		

	except:
		pass

#	print(k_st)
	count = 0
	
	# Checking for single elements
	for i in range(n):
		for j in range(m):
			if arr[i][j] >= k_st:
				count += 1

#	print(count)

	if n == m:
		var_arr = [0]*(n-1)*2
		print(var_arr)
		for i in range(len(var_arr)):
			if i%2 != 0:
				var_arr[i] = 1

		
		print(var_arr)

		while var_arr[

	i = 0
	j = 1
	
	while i<n-1 and j<m:
		k = 0
		l = 1
		while k<n-1 and l<m:
			s = arr[i][k] + arr[i][l] + arr[j][k] + arr[j][l]
			avg = float(s/4)
#			print(avg)
			if avg >= float(k_st):
				count += 1
			k += 1
			l += 1

		i += 1
		j += 1
		
	print(count)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
