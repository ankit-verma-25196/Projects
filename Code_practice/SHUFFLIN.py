# https://www.codechef.com/SEPT21C/problems/SHUFFLIN

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass

#	print(l1)

	count_even_1 = 0
	count_odd_1 = 0

	for i in range(n):
		if l1[i]%2 == 0:
			count_even_1 += 1
		else:
			count_odd_1 += 1

	
	
	count_even_2 = 0
	count_odd_2 = 0

	if n%2==0:
		count_even_2 = n//2
		count_odd_2 = n//2
	else:
		count_even_2 = n//2
		count_odd_2 = n//2+1

	total = min(count_even_2,count_odd_1) + min(count_odd_2,count_even_1)

	print(total)




	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
