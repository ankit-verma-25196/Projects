# Find Runner Up in the List
# Input - [2,3,6,6,5]
# Output - 5

# Input - [-10, 0 ,10]
# Output - 0


li = list(map(int,input().split()))

li.sort()
print(li)

li2 = list(set(li))
print(li2)

if len(li) == len(li2):
	print(li[len(li)-2])
else:
	li2.sort()
	print(li2[len(li2)-2])
