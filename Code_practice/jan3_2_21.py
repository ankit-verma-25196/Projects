import sys
import math

def solve():
	try:
		nm=list(map(int,input().split()))
		john_v=list(map(int,input().split())) # john votes
		jack_v=list(map(int,input().split())) # jack votes
	except:
		pass
	
	swaps = 0
	sum_john = 0
	sum_jack = 0

	for i in range(len(john_v)):
		sum_john=sum_john+john_v[i]
	for i in range(len(jack_v)):
		sum_jack=sum_jack+jack_v[i]

	while sum_john<=sum_jack:
		min_john=min(john_v)
		max_jack=max(jack_v)
		index_min=john_v.index(min(john_v))
		index_max=jack_v.index(max(jack_v))

#		print(str(min_john)+" "+str(max_jack))
		if min_john >= max_jack:
			swaps = -1
			break
		else:
			john_v[index_min]=max(jack_v)
			jack_v[index_max]=min(john_v)

			swaps = swaps + 1

			sum_john = sum_john - min_john
			sum_jack = sum_jack - max_jack
			
			sum_john = sum_john + max_jack
			sum_jack = sum_jack + min_john
			
			

	print(swaps)


try:
	for tc in range(int(input())):
		solve()
except:
	pass

