import sys
import math

def solve():
	try:
		n= int(input())	
		l1=list(map(int,input().split()))
	except:
		pass
	
#	print(l1)
	l2=list(set(l1))

#	print(l2)

	l2.sort()

#	print(l2)

	l=len(l2)

#	print(l)
	

	#checking the frequency of a number in a list
	#creating empty dictionary for holding the counts corresponding to that number
	freq={}
	for i in l1:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1 

	
	if l == 1:
		print("0")
	elif l == 2:

		# take third number that number whose frequency is higher out of two
		# if frequency is same , then take any of the two
#		print("two,check frequency")
		if freq[l2[0]] > freq[l2[1]]:
			#Take l2[0] two times in the triplet
			s= abs(l2[0]-l2[0])+abs(l2[0]-l2[1])+abs(l2[1]-l2[0])
			print(s)
		elif freq[l2[1]] > freq[l2[0]]:
			#Take l2[1] two times in the triplet
			s= abs(l2[0]-l2[1])+abs(l2[1]-l2[1])+abs(l2[1]-l2[0])
			print(s)
		elif freq[l2[1]] == freq[l2[0]]:
			s= abs(l2[0]-l2[0])+abs(l2[0]-l2[1])+abs(l2[1]-l2[0])
			print(s)

	elif l == 3:
		s= abs(l2[0]-l2[1])+abs(l2[1]-l2[2])+abs(l2[2]-l2[0])
		print(s)

	elif l > 3:
		if l % 2 == 0:
			half=int(l/2)
#			print(half)
			s= abs(l2[0]-l2[half])+abs(l2[half]-l2[l-1])+abs(l2[l-1]-l2[0])
			print(s)
		else:
			half=int(l/2)
#			print(half)
			s= abs(l2[0]-l2[half])+abs(l2[half]-l2[l-1])+abs(l2[l-1]-l2[0])
			print(s)

try:
	for tc in range(int(input())):
		solve()
except:
	pass



#1 2 4 6

#1 2 6 -- 1-2 2-6 6-1 1+4+5=10

#1 4 6 -- 1-4 4-6


#1 2 4 6 7 9 - len=6 , middle no's=4,6

#1 4 9


#1 2 4 6 7 - len=5 , middle no's=4
