import sys
import math

def solve():
	try:
		str1=input()
	except:
		pass
	
	count=0	
	i=0
	len1=len(str1)-1
	while (i<len1):
#		print(str1[i])
		if(str1[i]!=str1[i+1]):
			count+=1
			i+=2
		else:
			i+=1
#		print("I, Count = "+str(i)+","+str(count))
		
	print(count)	


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
