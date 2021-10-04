#Lapindromes


def solve():
	try:
		s = input()
	except:
		pass

	n = len(s)
#	print(s)
	i = 0
	d1 = {}
	while i < n//2:
#		print(s[i])
		d1[s[i]] = 0
		i += 1

	i = 0
	while i < n//2:
#		print(s[i])
		d1[s[i]] += 1
		i += 1

#	print(d1)

#	print("Checking for second half......")
	i = 0
	if n%2 == 0:
		i = int(n/2)
	else:
		i =int(n/2) + 1

#	print("i="+str(i))
	d2 = {}
	while i < n:
#		print(s[i])
		d2[s[i]] = 0
		i += 1

#	print("d2 = "+str(d2))
	i = 0
	if n%2 == 0:
		i = n//2
	else:
		i =n//2 + 1

#	print("i="+str(i))

	while i < n:
#		print(s[i])
		d2[s[i]] += 1
		i += 1

#	print("d2 = "+str(d2))

	li_d1 = list(d1.keys())
	li_d2 = list(d2.keys())

#	print(li_d1)
#	print(li_d2)

	li_d1.sort()
	li_d2.sort()

#	print(li_d1)
#	print(li_d2)

	flag1 = 0
	for i in range(len(li_d1)):
		if li_d1[i] != li_d2[i]:
			flag1 = 1
			break

	if flag1 == 1:
#		print("Flag 1")
		print("NO")
	else:
		
		flag2 = 0
		for i in range(len(li_d1)):
			if d1[li_d1[i]] != d2[li_d2[i]]:
				flag2 = 1
				break
		if flag2 == 1:
			print("NO")
		else:
			print("YES")

	

try:
	for tc in range(int(input())):
		solve()
except:
	pass
