# Recurring decimal inside bracket
import collections
n1 = int(input())
d1 = int(input())

n = n1/d1
print(n)

whole_part = str(n).split(".")[0]
decimal_part = str(n).split(".")[1]

#print(whole_part)
#print(decimal_part)

decimal_list = []

for i in decimal_part:
	decimal_list.append(i)

decimal_occurences = dict(collections.Counter(decimal_list))

final_decimal_string = ""
for i in decimal_occurences:
	if decimal_occurences[i] == 1:
		final_decimal_string += i
	else:
		more_occurences = "("+i+")"
		final_decimal_string += more_occurences


	
print(whole_part+"."+final_decimal_string)


