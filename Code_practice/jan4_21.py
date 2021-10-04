# Billiard table/Pool Table problem
import sys
import math

def angle45Cal(x,y):	
	x=x+1
	y=y+1
	return x,y

def angle135Cal(x,y):
	x=x-1
	y=y+1
	return x,y

def angle225Cal(x,y):
	x=x-1
	y=y-1
	return x,y

def angle315Cal(x,y):
	x=x+1
	y=y-1
	return x,y

	
def solve():
	try:
		nkxy=list(map(int,input().split()))
	except:
		pass
	n=nkxy[0]
	k=nkxy[1]
	x=nkxy[2]
	y=nkxy[3]

	cnt=0
	angle=45 # Initial angle is always 45 degree
	direc='u' # Initial direction is always "Up"-'u'
	prevX=None # Inital Previous X is not known

	x1=None
	x2=None
	x3=None
	x4=None
	y1=None
	y2=None
	y3=None
	y4=None

	c1=0
	c2=0
	c3=0
	c4=0

	corner = 0
	
	rem = k%4
	if rem == 0:
		k=4
	else:
		k=rem

	while cnt <= k+1:

		
#		if x == 0 and y == n or x == n and y == 0 or x == n and y == n: This condition will not appear as written in problem
			
		if cnt == 0:
			x,y=angle45Cal(x,y)
			cnt=cnt+1 # increasing the count for number of times
#			print("First Angle = "+str(angle))
#			print(str(x)+","+str(y))
		else:
			
			if (x == 0 or x == n) and (y == 0 or y == n):
#				print(str(x)+" "+str(y))
				corner = 1
#				print(str(x)+","+str(y)+" ....Breaking out of loop as it is one of the corner")
				break
			else:
#				Checking - whether angle has to be changed - Whether one of wall has hit
				if x == 0 and direc == 'u':
					prevX = x
					angle = 45
					cnt=cnt+1
				elif x == 0 and direc == 'd':
					prevX = x
					angle = 315
					cnt=cnt+1
				elif y == 0 and prevX == 0:
					angle = 45
					direc = 'u'
					cnt=cnt+1
				elif y == 0 and prevX == n:
					angle = 135
					direc = 'u'
					cnt=cnt+1
				elif x == n and direc == 'u':
					prevX = x
					angle = 135
					cnt=cnt+1
				elif x == n and direc == 'd':
					prevX = x
					angle = 225
					cnt=cnt+1
				elif y == n and prevX == 0:
					angle = 315
					direc = 'd'
					cnt=cnt+1
				elif y == n and prevX == n:
					angle = 225	
					direc = 'd'
					cnt=cnt+1	

				
				if cnt == 2:
#					print("cnt="+str(cnt)+" x/y="+str(x)+"/"+str(y))
					c1=c1+1
					if c1 == 1:
						x1=x
						y1=y
				elif cnt == 3:
#					print("cnt="+str(cnt)+" x/y="+str(x)+"/"+str(y))
					c2=c2+1
					if c2 == 1:
						x2=x
						y2=y
				elif cnt == 4:
#					print("cnt="+str(cnt)+" x/y="+str(x)+"/"+str(y))
					c3=c3+1
					if c3 == 1:
						x3=x
						y3=y
				elif cnt == 5:
#					print("cnt="+str(cnt)+" x/y="+str(x)+"/"+str(y))
					c4=c4+1
					if c4 == 1:
						x4=x
						y4=y

				

				if angle == 45:
					x,y=angle45Cal(x,y)
				elif angle == 135:
					x,y=angle135Cal(x,y)
				elif angle == 225:
					x,y=angle225Cal(x,y)
				elif angle == 315:
					x,y=angle315Cal(x,y)

#				print("Angle="+str(angle)+" x,y="+str(x)+","+str(y))


	if corner == 1:
		print(str(x)+" "+str(y))
	else:
		if k%4 == 0:
			print(str(x4)+" "+str(y4))
		elif k%4 == 1:
			print(str(x1)+" "+str(y1))
		elif k%4 == 2:
			print(str(x2)+" "+str(y2)) 
		elif k%4 == 3:
			print(str(x3)+" "+str(y3))


				
			
		

try:
	for tc in range(int(input())):
		solve()
except:
	pass
