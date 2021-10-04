import math
import sys

def solve():
	try:
		UVAS = list(map(int,input().split()))	
	except:
		pass

	U = UVAS[0]
	V = UVAS[1]
	A = UVAS[2]
	S = UVAS[3]

	
	if U == 1 and V == 1:
		print("Yes")
	else:
		v_sq = pow(U,2) - (2*A*S)
		
#		print(format(math.sqrt(v_sq), '.2f'))
#		print(float(A))

		if math.sqrt(v_sq) > float(V):
			print("No")
		else:
			print("Yes")
try:
	for tc in range(int(input())):
		solve()
except:
	pass
