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

#	print(str(lk)+" "+str(ld))
	if keyboards[lk-1] >= b or drives[ld-1] >= b:
        	print("-1")
	else:
		num = keyboards[lk-1]+drives[ld-1]
#		print(num)
		if num <= b:
			print(num)
		elif num > b:
			if keyboards[lk-1] > drives[ld-1]:
				print("Keyboards")
				find = 0
				i = 0
				while i<= ld-2 :
					print(str(drives[i]))
					newnum=drives[i]+keyboards[lk-1]
					if newnum > b:
						find=drives[i-1]+keyboards[lk-1]
						
						break
					elif newnum == b:
						find=drives[i]+keyboards[lk-1]
						break
					i=i+1
				if find == 0:
					find=drives[0]+keyboards[lk-1]
				print(find)
			else:
				print("Drives")
				find=0
				i = 0
				while i<= lk-2 : 
					print(str(keyboards[i]))
					newnum=keyboards[i]+drives[ld-1]
					if newnum > b:
						find=keyboards[i-1]+drives[ld-1]
						break
					elif newnum == b:
						find=keyboards[i]+drives[ld-1]
						break
					i=i+1
				if find == 0:
					find=keyboards[0]+drives[ld-1]
				print(find)

					
try:
	for tc in range(int(input())):
		solve()
except:
	pass
