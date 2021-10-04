#count substrings starting and ending with 1

def solve():
	try:
		n = int(input())
		s = input()
	except:
		pass

	l = 0
	r = 0
	count_one = 0
	count_sub = 0
	# Trying to use 2 pointer approach
	while r < n:
		if s[r] == '1':
			count_one += 1
			count_sub += count_one
		 
		r += 1

	print(count_sub)
try:
	for tc in range(int(input())):
		solve()
except:
	pass
