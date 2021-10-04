import math
n = int(input())
num_trailing_zeroes = 0
p = 1

while True:
	divisor = pow(5,p)
#	print("Divisor = ",divisor)
	zeroes =  n//divisor
	num_trailing_zeroes +=zeroes
	if zeroes == 0:
		break
	p += 1
			
		
#print(math.factorial(n))
print(num_trailing_zeroes)

