# Think on case - UDUDUDDU giving 3 but should be 1
# Problem : count valleys

def solve():
	try:
		steps = int(input())
		path = str(input())
	except:
		pass
	count = 0
	valleys = 0
	for i in range(len(path)):
		if path[i] == "D":
			if count == 0:
				valleys = valleys+1
			count = count-1
		elif path[i] == "U":
			count = count+1		
		
		print("Count = "+str(count))
		
	print(valleys)

try:
	for tc in range(int(input())):
		solve()
except:
	pass

