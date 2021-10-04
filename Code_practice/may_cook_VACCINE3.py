# https://www.codechef.com/COOK129C/problems/VACCINE3

def solve():
	try:
		l1 = list(map(int,input().split()))
	except:
		pass

	g = l1[0] # group no. of chef
	p = l1[1] # total population
	
	l2 = l1[2:13]
	print(g)
	print(p)
	print(l2)

	# calculate nim and max number of days for chef to get vaccinated

	flag = 0
	i = 9
	s = 0
	
	while i >= g-1 :
		s += l2[i]
		print("s="+str(s))
		i -= 1
		
	print("groups done ="+str(9-i))
	print("i="+str(i))
try:
	for tc in range(int(input())):
		solve()
except:
	pass
