def stock_span(li):
	n = len(li)
	st = []
	res = [1]*n
	st.append(0)
	for i in range(1, n):
		while not len(st) == 0 and li[st[-1]] <= li[i]:
			st.pop()
		if len(st) == 0:
			res[i] = i+1
		else:
			res[i] = i -st[-1]

		st.append(i)

	return res

li = [int(x) for x in input().split()]
print(stock_span(li))

