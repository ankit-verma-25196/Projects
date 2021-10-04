# Rotate the List and Return the final List after rotating for k steps
# [1,2,3,4,5,6,7] -> after k=3 rotations [5,6,7,1,2,3,4]
# Steps will be:
# 1. Reverse the whole list - [7,6,5,4,3,2,1]
# 2. Then Reverse from 0-k(k length), start=0 and end=k [5,6,7]
# 3. Then Reverse from k+1,n(n-k length), start=k+1 and end=n

# s->start of the arr to be sorted
# e->end of the arr to be sorted
def reverse(arr,s,e):
	temp = 0
	while s<=e:
		temp = arr[s]
		arr[s] = arr[e]
		arr[e] = temp
		s+=1
		e-=1


def rotate_by_k_steps(arr,k):
	n = len(li)
	k = k%n
	reverse(arr,0,n-1)
	reverse(arr,0,k-1)
	reverse(arr,k,n-1)


li = [int(x) for x in input().split()]
k = int(input())
print("before rotating = ",li)
rotate_by_k_steps(li,k)
print("after rotating = ",li)
		
