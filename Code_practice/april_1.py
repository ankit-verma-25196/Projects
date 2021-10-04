import sys
import math

abc = ""
try:
	abc = list(map(int,input().split()))
except:
	pass

#print(abc)
if len(abc) == len(set(abc)):
	print("NO")
else:
	print("YES")
