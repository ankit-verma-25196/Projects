# amazon sorting prioritizing algo
'''
Sample input:
[zid 93 12]
[fp kindle book]
[10a echo show]
[17g 12 25 6]
[ab1 kindle book]
[125 echo dot second generation]
'''
def sortOrders(orderList):
	print(orderList)

	primes = []
	primes_final = []
	nonPrimes = []
	for s in orderList:
		arr = s.split()
		print(arr)
		if arr[1].isalpha():
			res1 = "".join(arr[1:])
			res2 = " ".join(arr)
			print("res = "+res1)
			primes.append(res1)
			primes_final.append(res2)
		else:
			nonPrimes.append(s)


	print()
	print("final")
	print(primes)
	print(nonPrimes)
	print(primes_final)

	primes.sort()
	primes_final.sort()

	print(primes)
	print(primes_final)

	h1 = {}
	for s in primes:
		if  s in h1:
			h1[s] += 1
		else:
			h1[s] = 1

	print(h1)
			
	for s in h1.keys():
		if h1[s] > 2

	
			
try:
	for tc in range(int(input())):
		n = int(input())
		orderList = []
		while n >0:
			s = input()
			orderList.append(s)
			n -= 1

		sortOrders(orderList)

except:
	pass
