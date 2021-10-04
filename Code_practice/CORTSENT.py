# https://www.codechef.com/START4C/problems/CORTSENT

def solve():
	try:
		li = list(map(str, input().split()))
	except:
		pass

	k = int(li[0])
	rulebreak = 0
	for i in range(k):
		flag = 0
		for ch in li[i+1]:
			# chracter should be between [a-m]<--flag= 1 or [N-Z]<--flag=2
			if flag == 1:
				if (ord(ch)>= 78 and ord(ch)<=90):
					rulebreak += 1
					break
			if flag == 2:
				if (ord(ch)>= 97 and ord(ch)<=109):
					rulebreak += 1
					break
			if (ord(ch)>= 97 and ord(ch)<=109):
				# assign a flag
				flag = 1
			elif (ord(ch)>= 78 and ord(ch)<=90):
				flag = 2
			else:
				rulebreak += 1
				break
		if rulebreak > 0:
			break

	if rulebreak > 0:
		print("NO")
	else:
		print("YES")
			
				 
			
try:
	for tc in range(int(input())):
		solve()
except:
	pass

