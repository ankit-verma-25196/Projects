#List comprehensions

li1 = [2*i for i in range(1,10)]

print(li1)

x = 1
y = 1
z = 1
n = 2

outer_list = []
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			inner_list = []
			if i+j+k != n:
				inner_list.append(i)
				inner_list.append(j)				
				inner_list.append(k)

				outer_list.append(inner_list)


print(outer_list)

#using List Comprehensions

outer_list_2 = [[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(outer_list_2)




