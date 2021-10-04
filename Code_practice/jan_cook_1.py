import sys
import math

def solve():
	try:
		s = str(input())
	except:
		pass

	
	l=len(s)
#	print(l)
	
	if l < 10:
		print("NO")
	else:
		small = 0
		capital = 0
		number = 0
		special = 0
		for i in s:
			if i.islower():
				small = small +1
			elif i.isupper():
				capital = capital +1
			elif i.isdigit():
				number = number +1
			elif i=='@' or i =='#' or i =='%' or i =='&' and i =='?':
				special = special +1

		print(str(small)+" "+str(cpaital)+" "+str(number)+" "+str(special))

		if small >0 and capital >0 and number >0 and special >0 :
			print("YES")

try:
	for tc in range(int(input())):
		solve()
except:
	pass


