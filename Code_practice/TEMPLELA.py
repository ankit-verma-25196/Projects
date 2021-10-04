# https://www.codechef.com/SDPCB21/problems/TEMPLELA

# 0 1 2 3 4 5 6
# 1 2 3 4 3 2 1

# n//2+1 = 4

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass

#	print(l1)

	if n % 2 == 0:
		print("no")
	else:
		if l1[0] == 1 and l1[n-1]==1:
			flag1 = 1
			for i in range(1,n//2+1):
				if l1[i] != l1[i-1]+1:
					flag1 = 0
					break
			flag2 = 1
			for i in range(n//2+1,n-1):
				if l1[i] != l1[i-1]-1:
					flag2 = 0
					break

			if flag1 == 1 and flag2 == 1:
				print("yes")
			else:
				print("no")
					
			
		else:
			print("no")


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
