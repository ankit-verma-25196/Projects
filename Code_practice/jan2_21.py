import sys
import math

def solve():
	try:
		n=int(input())
		s=str(input())
	except:
		pass

	s_hash={
		'0000':'a',
		'0001':'b',
		'0010':'c',
		'0011':'d',
		'0100':'e',
		'0101':'f',
		'0110':'g',
		'0111':'h',
		'1000':'i',
		'1001':'j',
		'1010':'k',
		'1011':'l',
		'1100':'m',
		'1101':'n',
		'1110':'o',
		'1111':'p'
	}
	
	i=0
	while i<len(s):
		print(s_hash[s[i:i+4]],end="")
		i=i+4
	print()
try:
	for tc in range(int(input())):
		solve()
except:
	pass

# a,b,c,d,e,f,g,h,i,j, k, l, m, n, o, p
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# '0000':a,'0001':'b','0010':'c','0011':'d','0100':'e','0101':'f','0110':'g','0111':'h','1000':'i','1001':'j','1010':'k','1011':'l','1100':'m','1101':'n','1110':'o','1111':'p'
