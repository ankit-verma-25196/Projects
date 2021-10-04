# April Cook 1

def solve():
	try:
		ambmcmtmabc = list(map(int,input().split()))
	except:
		pass

	am = ambmcmtmabc[0]
	bm = ambmcmtmabc[1]
	cm = ambmcmtmabc[2]
	tm = ambmcmtmabc[3]
	a = ambmcmtmabc[4]
	b = ambmcmtmabc[5]
	c = ambmcmtmabc[6]

	sumabc = a+b+c

	if a>=am and b>=bm and c>=cm and sumabc>=tm:
		print("YES")	
	else:
		print("NO")
try:
	for tc in range(int(input())):
		solve()
except:
	pass

