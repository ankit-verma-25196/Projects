import math
import sys

def solve():
	try:
		n = int(input())
	except:
		pass
	count1 = 0
	count2 = 0
 
	for i in range(n):
		l1 = []
		l1 = list(map(str,input().split()))
#		print(l1)			
		score1=0
		score2=0
#		print(l1[0])
#		print(l1[1])
		for k in range(len(l1[0])):
#			print(l1[0][k])
			score1+=int(l1[0][k])
		for k in range(len(l1[1])):
			score2+=int(l1[1][k])

#		print("Score1="+str(score1))
#		print("Score2="+str(score2))
		if(score1 > score2):	
			count1+=1
		elif(score2 > score1):
			count2+=1
		elif(score1 == score2):
			count1+=1
			count2+=1

	if(count1 > count2):
		print("0",end=" ")
		print(count1)
	elif(count2 > count1):
		print("1",end=" ")
		print(count2)
	elif(count1 == count2):
		print("2",end=" ")
		print(count1)

					

try:
	for tc in range(int(input())):
		solve()
except:
	pass
