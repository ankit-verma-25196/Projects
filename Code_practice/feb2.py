import sys
import math

def solve():
	try:
		p=str(input())
		n=int(input())
		output=""

		time_given=p.split(" ")
		hhmm=time_given[0].split(":")

#		print(time_given[1])

		if time_given[1]=="AM" and hhmm[0]=="12":
			hhmm[0]=int(0)

#		if time_given[1]=="PM" and hhmm[0]!="12":
		if time_given[1]=="PM":
			if hhmm[0]!="12":
				hhmm[0]=int(hhmm[0])+12

#		print("time given hour="+str(hhmm[0]))
#		print("time given minute="+str(hhmm[1]))

		
		for i in range(n):
			time=str(input())
			time_arr=time.split(" ")
#			print(time_arr[0])
#			print(time_arr[1])
#			print(time_arr[2])
#			print(time_arr[3])

			arr1=time_arr[0].split(":")
			arr2=time_arr[2].split(":")

			if time_arr[1]=="AM" and arr1[0]=="12":
				arr1[0]=int(0)

			if time_arr[3]=="AM" and arr2[0]=="12":
				arr2[0]=int(0)

	
			if time_arr[1] == "PM":
				if arr1[0]!="12":
					arr1[0]=int(arr1[0])+12
			if time_arr[3] == "PM":
				if arr2[0]!="12":
					arr2[0]=int(arr2[0])+12

#			print("arr1[0] hour="+str(arr1[0]))
#			print("arr2[0] hour="+str(arr2[0]))

#			print("arr1[1] minute="+str(arr1[1]))
#			print("arr2[1] minute="+str(arr2[1]))
				
			#check difference in start and end time
			diffHour=int(arr2[0]) - int(arr1[0])
			diffMin=int(arr2[1]) - int(arr1[1])

#			print("Diff Hour = "+str(diffHour))			
#			print("Diff Minute = "+str(diffMin))

#			if arr1[0]==int(arr2[0]) and int(arr1[1])==int(arr2[1]):
				
			if hhmm[0]==arr1[0] and hhmm[0]==arr2[0]:
				if int(hhmm[1]) >=int(arr1[1]) and int(hhmm[1]) <=int(arr2[1]):
					output=output+"1"
				else:
					output=output+"0"

			elif hhmm[0]==arr1[0] and hhmm[0]!=arr2[0]: # if hour given is equal to hour of start time
				# then check minute given should be greater than or equal to start minute
#				print(int(hhmm[1]))
#				print(int(arr1[1]))
				if int(hhmm[1]) >=int(arr1[1]):
					output=output+"1"	
				else:
					output=output+"0"

			elif hhmm[0]!=arr1[0] and hhmm[0]==arr2[0]: # if hour given is equal to hour of end time
				# then check minute given should be less than or equal to end minute
#				print(int(hhmm[1]))
#				print(int(arr2[1]))
				if int(hhmm[1]) <=int(arr2[1]):
					output=output+"1"	
				else:
					output=output+"0"

			elif (int(hhmm[0]) > int(arr1[0])) and (int(hhmm[0]) < int(arr2[0])):
				# then in this case it's not necessary to check the minute , it will always lie inside the time limit
			
				output=output+"1"
			else:
#				print("hello2")
				output=output+"0"

#			print(output)
		print(output)
				
	except:
		pass

	
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass


#12:30 PM
#4
#01:00 PM 12:00 AM
#01:00 PM 12:31 PM        
#12:31 PM 12:31 PM
#12:32 PM 12:31 PM
#0100
#Expected = 0111

# To follow below, convert 12:00 AM to 24:00 hr to get correct difference
# if diff is =>24 , then always 1
# if diff is < 24
# -- if diff is <24 and >12
# -- if diff is =12
# -- if diff is <12


