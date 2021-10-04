# factorial using recursion

def factorial(x):
	
	# base case - we know factorial of 0 is 1
	if x == 0:
		return 1

	else:
		return x*factorial(x-1)


x = int(input())
print(factorial(x))

