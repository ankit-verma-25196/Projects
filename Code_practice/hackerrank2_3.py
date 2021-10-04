import sys
import math

def solve():
	try:
		bnm=list(map(int,input().split()))
		keyboards=list(map(int,input().split()))
		drives=list(map(int,input().split()))
	except:
		pass
	b=bnm[0]
	checkPrice=0
	for i in range(len(keyboards)):
		for j in range(len(drives)):
			totalPrice=keyboards[i]+drives[j]
			if totalPrice > checkPrice and totalPrice <=b:
				checkPrice=totalPrice
	if checkPrice==0:
		print("-1")
	else:
		print(checkPrice)


try:
	for tc in range(int(input())):
		solve()
except:
	pass

# Points to Remember:

# Time Complexity is n^2
# Before storing values in new array, check whether it can be done storing in single variable
# Think about simple solutions
