def solve():	
	h1 = {}
        base = 64
        for i in range(1,27):
            h1[i]=chr(base+i)
        h1[0]='Z'
        print(h1)
            
        temp = columnNumber
        if temp <27:
            return h1[temp]
        else:
            s = ""
            while temp >= 26:
                rem = temp%26
                s = s + h1[rem]
                temp = temp//26
                if temp % 26 == 0:
                    temp -= 1
            print(temp)
            s = s + h1[temp]
            return s[::-1]
try:
	for tc in range(int(input())):
		n = int(input())
		print(solve(n))
except:
	pass

