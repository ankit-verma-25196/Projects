# https://www.codechef.com/UADS1001/problems/GOLDTRIP

def solve():
	try:
		n = int(input())
		l1 = list(map(int, input().split()))
	except:
		pass

	prefix_arr = [0]*n

	for i in range(n):
		prefix_arr[i] = prefix_arr[i-1] + l1[i]
	
	try:
		q = int(input())

		for i in range(q):
			q1q2 = list(map(int, input().split()))
			q1 = q1q2[0]
			q2 = q1q2[1]
			
#			print(prefix_arr[q2-1])
#			print(prefix_arr[q1-1])
			s = prefix_arr[q2-1] - prefix_arr[q1-1] + l1[q1-1]

			print(s)
	except:
		pass


try:
	for tc in range(int(input())):
		solve()
except:
	pass
