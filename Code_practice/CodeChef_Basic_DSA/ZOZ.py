# codeChef Basic Data Structures - Magic Elements 
# https://www.codechef.com/UADS1001/problems/ZOZ

def solve():
	try:
		nk = list(map(int,input().split()))
		l1 = list(map(int,input().split()))
	except:
		pass
	
	n = nk[0]
	k = nk[1]

	total_sum = 0
	for i in range(n):
		total_sum += l1[i]

	num = 0
#	print(total_sum)
	
	for i in range(n):
		if l1[i]+k > total_sum-l1[i]:
			num += 1

	print(num)
	
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
