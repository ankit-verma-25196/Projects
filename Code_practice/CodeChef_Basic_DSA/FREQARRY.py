# codeChef Basic Data Structures - frequency array
# https://www.codechef.com/UADS1001/problems/FREQARRY

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass
	
	l2 = list(set(l1))
	
	if len(l1) == len(l2):
		print("prekrasnyy")
	else:
		print("ne krasivo")

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
