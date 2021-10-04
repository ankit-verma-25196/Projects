# Pattern matching using Rabin-Karp Algorithm

def search(pat,text,q):
	n = len(text)
	m = len(pat)

	d = 256

	# hash value of pattern
	p = 0

	# hash value of text
	t = 0
	h = 1

	for i in range(m-1):
		h = (h*d)%q

	# calc. hash value of pattern
	# calc. hash value of first window
	for i in range(m):
		p = (d*p + pat[i])%q
		t = (d*t + text[i])%q

	# slide the pattern over the text - window by window
	for i in range(n-m+1):
		# check hash value of current window of text and pattern

		# case of collision
		if p == t:
			for j in range(m):
				if text[i+j] != pat[j]:
					break
			if j == m:
				print("Collision, String Found at = "+str(i))

		# calc. hash value of next window of text
		# remove the first digit and add last 1 in end
		if i < n-m:
			t = (d*(t-text[i]*h)+text[i+m])%q

		# for making hash value always positive
		if t < 0:
			t = t+q

			

def solve():
	try:
		text = input()
		pat = input()
	except:
		pass

	q = 101
	search(pat,text,q)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
