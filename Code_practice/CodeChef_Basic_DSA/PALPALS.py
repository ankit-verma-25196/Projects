# https://www.codechef.com/UADS1001/problems/PALPALS

def solve():
	try:
		s = input()
	except:
		pass

	dic1 = {}
	for i in s:
		if i in dic1.keys():
			dic1[i] += 1
		else:
			dic1[i] = 1

#	print(dic1)
	# count the frequency

	odd = 0
	even_pairs = 0
	for i in dic1.keys():
		if dic1[i] % 2 == 0:
			div = dic1[i] // 2
			even_pairs += div
		else:
			odd += 1
			div = dic1[i] // 2
			even_pairs += div

#	print(even_pairs)
#	print(odd)

	if odd > even_pairs:
		print("NO")
	else:
		print("YES")

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
