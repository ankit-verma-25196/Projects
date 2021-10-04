

def solve():
	try:
		Mxy = list(map(int, input().split()))
		l1 = list(map(int, input().split()))
	except:
		pass

	M = Mxy[0]
	x = Mxy[1]
	y = Mxy[2]

	dist = x*y

	l1.sort()

	min_ = l1[0]-dist
	if min_ <= 0:
		min_ = 1
	max_ = l1[0]+dist
	if max_ > 100:
		max_ = 100

	if min_ == 1 and max_ == 100:
		print("0")

	else:
		l = len(l1)
		i = 1
		houses = 0
		if min_ != 1:
			diff = min_ - 1
			print("first diff = "+str(diff))
			houses += diff

		while i<l:
			min_new = l1[i]-dist
			max_new = l1[i]+dist

	
			if min_new > max_:
				diff = min_new - max_ -1
				print("diff = "+str(diff))
				houses += diff
			max_ = max_new


			i += 1
	
		print("last max ="+str(max_))
		if max_ < 100:
			diff = 100- max_
			print("last diff = "+str(diff))
			houses += diff
		print(houses)

	

try:
	for tc in range(int(input())):
		solve()
except:
	pass

