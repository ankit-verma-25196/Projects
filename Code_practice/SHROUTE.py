# https://www.codechef.com/JUNE21C/problems/SHROUTE

def solve():
	try:
		nm = list(map(int,input().split()))
		a = list(map(int,input().split()))
		b = list(map(int,input().split()))
	except:
		pass

	n = nm[0]
	m = nm[1]

	MAX = 1000000007
	d1 = {}

#	print(d1)

	i = 0
	while i<n:
		if i == 0:
			d1[i] = 0
		elif a[i] != 0:
			d1[i] = 0
		else:
			d1[i] = MAX
		i += 1

#	print(d1)

	i = 0
	right = -1
	while i<n:
		if a[i] == 1:
			right = i
		if right != -1:
			if a[i] == 0:
				d1[i] = min(d1[i],i-right)
			
		i += 1
	
#	print(d1)

	i = n-1
	left = -1
	while i >= 0:
		if a[i] == 2:
			left = i
		if left != -1:
			if a[i] == 0:
				d1[i] = min(d1[i],left-i)
		i -= 1	

#	print(d1)

	# Output
	i = 0
	while i<m:
		j = b[i] - 1
		if d1[j] != MAX:
			print(d1[j],end=" ")
		else:
			print("-1",end=" ")

		i += 1

	print()

try:
	for tc in range(int(input())):
		solve()
except:
	pass
