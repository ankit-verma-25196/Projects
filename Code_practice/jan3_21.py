import sys
import math

def solve():
	try:
		nm=list(map(int,input().split()))
		john_v=list(map(int,input().split())) # john votes
		jack_v=list(map(int,input().split())) # jack votes
	except:
		pass
	
	sum_john=0
	sum_jack=0

	for i in range(len(john_v)):
		sum_john=sum_john+john_v[i]
	for i in range(len(jack_v)):
		sum_jack=sum_jack+jack_v[i]
#	print(sum_john)
#	print(sum_jack)

		
	if sum_john>sum_jack:
		print("0")
	elif sum_john==sum_jack:
		print("-1")
	elif sum_john<sum_jack:
		if len(set(john_v))==1 and len(set(jack_v))==1:
			print("Same Elements,Used set() function")
			l=len(john_v)
			op_cnt = 0
			flag=0
			while l > 0:
				sum_john=sum_john-john_v[0]
				sum_jack=sum_jack-jack_v[0]
	
				sum_john=sum_john+jack_v[0]
				sum_jack=sum_jack+john_v[0]
				op_cnt=op_cnt+1
				if sum_john > sum_jack:
					flag=1
					break
				else:
					l=l-1

			if flag==0:
				print("-1")
			else:
				print(op_cnt)
		else:
			print("Different Elements, not using set()")
			john_v.sort()
			jack_v.sort()
			j=len(jack_v)-1
#			print(j)
			op_cnt = 0
			flag=0
			for i in range(len(john_v)):
				sum_john=sum_john-john_v[i]
				sum_jack=sum_jack-jack_v[j]
	
				sum_john=sum_john+jack_v[j]
				sum_jack=sum_jack+john_v[i]
				op_cnt=op_cnt+1
				if sum_john > sum_jack:
					flag=1
					break
				else:
					j=j-1

			if flag==0:
				print("-1")
			else:
				print(op_cnt)


try:
	for tc in range(int(input())):
		solve()
except:
	pass

'''
2 3
2 2 - john
5 5 5 - jack

can intially --> john votes > jack votes? --> yes, output 0 in that case as "0" operations needed.

Case when john can't be winner -->If after swapping all the available votes of john with highest number of votes avilable with jack,even then sum_john<sum_jack


4 3
1 3 2 4 - john
6 7 8 - jack

1 2 3 4
6 7 8

Case - 
when len(jack_array) > len(john_array), which array to be taken in logic loop-->is should be considered or not?

TRY with test cases input file,with large sets of data

'''
