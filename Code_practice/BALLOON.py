# https://www.codechef.com/COOK130C/problems/BALLOON

def solve():
	try:
		n = int(input())
		li = list(map(int,input().split()))
	except:
		pass

	count = 0
	flag = 0
	i = 0
	while i<len(li):
		if count == 7:
			flag = 1
			break
		if li[i]>=1 and li[i]<=7:
			count += 1

		i += 1
#			print(count)	
#		else:
#			print("NO")

	print(i)

	'''
	if i == n-1:
		print(i+1)
	else:
		print(i-1)
	'''	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
