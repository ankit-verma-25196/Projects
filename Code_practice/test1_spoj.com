
try:
	n = int(input())
	if n != 42:
		print(n)
		
