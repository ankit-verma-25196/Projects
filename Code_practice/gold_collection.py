# gold collection - codechef

def solve():
	try:
		n = int(input())
		li = list(map(int, input().split()))
		q = int(input())
	except:
		pass


	# calculating the Prefix sum arr - going n iterations only 1 time
	pre_sum = list(li)
	for i in range(1,n):
		pre_sum[i] = pre_sum[i] + pre_sum[i-1]
		

#	print(pre_sum)
#	print(li)

	
	while q>0:
		try:
			r = list(map(int, input().split())) # Range Array
		except:
			pass

#		print(r[0])
#		print(r[1])

		s = pre_sum[r[1]-1]-pre_sum[r[0]-1]+li[r[0]-1] # O(1)
		
		'''
		for i in range(r[0],r[1]+1):
#			print(i) 		# O(n)
			s += li[i-1]
		'''

		print(s)

	
		
		q-=1
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
