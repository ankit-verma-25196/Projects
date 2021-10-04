import sys
import math


tc=int(eval(input()))


while(tc>0):
	
	n=int(eval(input()))
	list1=[]
	list1 = list(map(str,input().split()))
	list2=[0]*len(list1)
	y=0
	for x in range(len(list1)-1):
#		print("\nX="+str(x)+"\n")
		diff=int(list1[x+1])-int(list1[x])
#		print("\nDifference="+str(diff)+"\n")
		if(diff<=2):
			list2[y]=list2[y]+1
			if(x==len(list1)-2):
				list2[y]=list2[y]+1	
		else:
			list2[y]=list2[y]+1
			y=y+1
	count=0
	list3=[]
	for a in range(len(list2)):
		if(list2[a]>0):
			count=count+1
			list3.append(list2[a])
	if(count>1):
		max=list3[0]
		min=list3[0]
		for k in range(len(list3)-1):
			if(list3[k+1]>list3[k]):
				max=list3[k+1]
			if(list3[k+1]<list3[k]):
				min=list3[k+1]
		print(str(min)+" "+str(max)+"\n")
	else:
		print(str(list2[0])+" "+str(list2[0])+"\n")
		
#	print("\nlist1="+str(list1)+"\n")
#	print("\nlist2="+str(list2)+"\n")
	
	tc=tc-1

#End of the program
