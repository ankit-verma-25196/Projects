import math
import sys

def solve():
	list1 = []
	list1 = list(map(str,input().split()))
	n=int(list1[0])
	k=int(list1[1])
	list2 = []
	list2 = list(map(str,input().split()))
	s1=0
	s2=0
	count=0
	for x in range(len(list2)):
		s1+=int(list2[x])
		if(int(list2[x])>k):
			s2+=k
			count+=1
		else:
			s2+=int(list2[x])
	if(count==0):
		print(count)
	else:
#		print("\n"+str(s1)+" "+str(s2)+"\n")
		diff=s1-s2
		print(diff)
try:
	for tc in range(int(input())):
		solve()
except:
	pass



