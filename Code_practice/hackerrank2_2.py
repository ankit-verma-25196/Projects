#Problem : electronic shop - find most expensive items to be find out of 2 priced items

def solve():
	try: 
		bnm=list(map(int,input().split()))
		b=bnm[0]
		keyboards=list(map(int,input().split()))
		drives=list(map(int,input().split()))
	except:
		pass

	keyboards.sort()
	drives.sort()
#	print(str(keyboards)+" "+str(drives))
	lk=len(keyboards)
	ld=len(drives)
	sums=[]
#	print(str(lk)+" "+str(ld))
	find=0
	isum = keyboards[0]+drives[0]
	print(isum)
	if keyboards[0]+drives[0] > b:
        	print("-1")
	else:
		check=0
		for i in range(len(keyboards)):
			for j in range(len(drives)):
				s=keyboards[i]+drives[j]
				sums.append(s)
				if s == b:
					check=1
					break
				elif s > b:
					break
	

		if check == 1:
			print(b)
		else:
			sums.sort()
			print(sums)
			for j in range(len(sums)):
				if sums[j] == b:
					break
				elif sums[j] > b:
					break

			if j==len(sums)-1 and sums[j] < b:
				print(sums[j])
			else:
				print(sums[j-1])

					
try:
	for tc in range(int(input())):
		solve()
except:
	pass



