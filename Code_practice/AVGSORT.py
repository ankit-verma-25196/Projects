# https://www.codechef.com/problems/AVGSORT

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass

#	print(l1)

	# Check if sequence is decreasing or not
	cnt = 0
	for i in range(n-1):
		if l1[i]>=l1[i+1]:
			cnt += 1

#	print(cnt)		

	if cnt == n-1:
		print("No")
	else:
		print("Yes")
try:
	for tc in range(int(input())):
		solve()
except:
	pass
