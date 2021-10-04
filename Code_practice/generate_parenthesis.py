# generate balanced parenthesis for n input
import pdb

def _solve(s, n):
	if n >0:
		solve(s,0,n,0,0)
	return


def solve(s,pos,n,open_,close):

	print(open_)
	print(close)
	if close == n:
		for i in s:
			print(i,end="")
		print()
		return


	if open_>close:
		s[pos] = ')'
		solve(s,pos+1,n,open_,close+1)

	
	if open_>n:
		s[pos] = "("
		solve(s,pos+1,n,open_+1,close)
	

try:
	n = int(input())
	s = ""
	print("s="+s)
	_solve(s,n)
except:
	pass

