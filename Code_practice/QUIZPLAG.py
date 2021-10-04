# https://www.codechef.com/START4C/problems/QUIZPLAG

def solve():
	try:
		nmk = list(map(int, input().split()))
		exams = list(map(int, input().split()))
	except:
		pass
	n = nmk[0]
	m = nmk[1]
	k = nmk[2]

	h1 = {}
	x = 0
	for i in exams:
		if i in h1.keys():
			h1[i] += 1	
		else:
			h1[i] = 1
		x += 1

#	print(h1)
	cnt = 0
	arr = []
	for i in h1.keys():
		if i >=1 and i <=n:
			if h1[i] > 1:		
				cnt += 1
				arr.append(i)

	arr.sort()

	print(cnt, end= " ")
	for i in range(len(arr)):
		print(arr[i],end= " ")
	print()

	


try:
	for tc in range(int(input())):
		solve()
except:
	pass
