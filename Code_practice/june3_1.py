import sys
import math

def solve():
	try:
		n=int(input())
	except:
		pass
	lis1=[]
	lis1=list(map(int,input().split()))
#	for i in range(len(lis1)):
#		print("list["+str(i)+"]="+str(lis1[i]))
	
	if(lis1[0]!=5):
		print("NO")
	else:
		count1=0
		count2=0
		diff=0
		total=0
		div=0
		res=0
		for i in range(len(lis1)):
			if(lis1[i]==5):
				res+=1
				count1+=1
#				print("Count="+str(count1))
			else:
				if(lis1[i]==10):
					count2+=1
				diff=lis1[i]-5
				total1=count1*5
				total2=count2*10
#				print("diff,total="+str(diff)+","+str(total))
				if(diff==5):
					if(total1>0):
						if(diff>total1):
							res=0
							break
						elif(diff<total1):
							res+=1
							div=diff/5			
							count1-=div
#							print("res,div,count="+str(res)+","+str(div)+","+str(count1)+","+str(count2))
						elif(diff==total1):
							res+=1
							count1=0
#							print("res="+str(res))
					elif(total1==0):
						res=0
						break
						'''
						if(diff>total2):
							res=0
							break
						elif(diff<total2):
							res+=1
							div=diff/10			
							count2-=div
							print("res,div,count="+str(res)+","+str(div)+","+str(count1)+","+str(count2))
						elif(diff==total2):
							res+=1
							count2=0
							print("res="+str(res))
						'''
				elif(diff==10):
					if(total2>0):
						if(diff>total2):
							res=0
							break
						elif(diff<total2):
							res+=1
							div=diff/10			
							count2-=div
#							print("res,div,count="+str(res)+","+str(div)+","+str(count1)+","+str(count2))
						elif(diff==total2):
							res+=1
							count2=0
#							print("res="+str(res))
					elif(total2==0):
						if(diff>total1):
							res=0
							break
						elif(diff<total1):
							res+=1
							div=diff/5			
							count1-=div
#							print("res,div,count="+str(res)+","+str(div)+","+str(count1)+","+str(count2))
						elif(diff==total1):
							res+=1
							count1=0
#							print("res="+str(res))
						
					
		if(res==0):
			print("NO")
		elif(res>0):
			print("YES")	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
