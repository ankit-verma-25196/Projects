# find nth tribonacci number using recursion

def tribonacci(n):
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1
	else:
		return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

try:
	n = int(input())
	print(tribonacci(n))
except:
	pass
