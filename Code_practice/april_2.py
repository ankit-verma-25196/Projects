import sys
import math
import decimal

def solve():
	try:
		k1k2k3v = list(map(float,input().split()))	
	except:
		pass

	k1 = k1k2k3v[0]
	k2 = k1k2k3v[1]
	k3 = k1k2k3v[2]
	v = k1k2k3v[3]


	speed = k1*k2*k3*v

#	print(speed)
	

	time = 100/speed
#	time2 = format(time, '.3f')
#	print(time)
#	print(time2)

#	print(round(time,2))
	r_time = round(float(time),2)
#	print(r_time)
#	print(type(r_time))

	if r_time < 9.58:
		print("YES")
	else:
		print("NO")

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
