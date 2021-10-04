#tic tac toe Game
# CodeChef May 4 challenge

def solve():
	try:
		arr = []
		rows, cols = (3, 1)
		for i in range(rows):
			col = []
			for j in range(cols):
				s = input()
				col.append(s)
			arr.append(col)

	except:
		pass


	count_O = 0
	count_O_global = 0

	count_X = 0
	count_X_global = 0

	count_empty = 0 # Always Global

	# Variables to check win condition - same element in 1 row or column
	flag_all_O = 0 
	flag_all_X = 0

	for i in range(rows):
		count_O = 0
		count_X = 0


		# Checking 1 full row
		for j in range(cols):
			for k in range(rows):
				if arr[i][j][k] == 'X':
					count_X += 1
					count_X_global += 1
				elif arr[i][j][k] == 'O':
					count_O += 1
					count_O_global += 1
				elif arr[i][j][k] == '_':
				# Check count empty in Row only - Only once else duplicate count
					count_empty += 1
	
		if count_X == 3:
			flag_all_X += 1
		elif count_O == 3:
			flag_all_O += 1


		count_O = 0
		count_X = 0


		# Checking 1 full column
		for j in range(cols):
			for k in range(rows):
				if arr[k][j][i] == 'X':
					count_X += 1
				elif arr[k][j][i] == 'O':
					count_O += 1
		
		
		if count_X == 3:
			flag_all_X += 1
		elif count_O == 3:
			flag_all_O += 1

	'''
	print("flag_all_X = "+str(flag_all_X))
	print("flag_all_O = "+str(flag_all_O))
		
	print("Global Count X = "+str(count_X_global))
	print("Global Count O = "+str(count_O_global))
	print("Global Count Empty = "+str(count_empty))
	'''	

	X_diagonals = 0		
#	Checking for Diagonals of all X's
	if arr[0][0][0] == 'X' and arr[1][0][1] == 'X' and arr[2][0][2] == 'X':
		X_diagonals += 1
	if arr[0][0][2] == 'X' and arr[1][0][1] == 'X' and arr[2][0][0] == 'X':
		X_diagonals += 1

	O_diagonals = 0		
#	Checking for Diagonals of all O's
	if arr[0][0][0] == 'O' and arr[1][0][1] == 'O' and arr[2][0][2] == 'O':
		O_diagonals += 1
	if arr[0][0][2] == 'O' and arr[1][0][1] == 'O' and arr[2][0][0] == 'O':
		O_diagonals += 1

#	print("Diagonals..")
#	print("X_diagonals = "+str(X_diagonals))
#	print("O_diagonals = "+str(O_diagonals))

	# CONDITIONS..................................
	# Win condition for X
	if (flag_all_X == 1 and flag_all_O == 0) or (X_diagonals == 1 and O_diagonals == 0):
		if count_X_global-1 == count_O_global:
#			print("X WIN")
			print("1")
		else:
#			print("meX1")
			print("3")
	elif flag_all_X > 1 or X_diagonals > 1:
#		print("me5")
		print("3")
	# Win condition for O
	if (((flag_all_O == 1 and flag_all_X == 0) or (O_diagonals == 1 and X_diagonals == 0)) ):
		if count_X_global == count_O_global:
			print("1")
		else:
			print("3")
	elif flag_all_O > 1 or O_diagonals > 1:
#		print("me5")
		print("3")

	# Draw Condition
	if count_X_global == 5 and count_O_global == 4 and flag_all_O == 0 and flag_all_X == 0 and O_diagonals == 0 and X_diagonals == 0:
		print("1")
	# Neither Draw nor Win , Position is reachable and Game will Continue
	if flag_all_O == 0 and flag_all_X == 0 and O_diagonals == 0 and X_diagonals == 0 and count_empty > 0:
		if count_X_global-1 == count_O_global or count_X_global == count_O_global:
			print("2")
		# Not Reachable Conditions
		else:
#			print("meX2")
			print("3")
		'''
		elif flag_all_O > 0 and flag_all_X > 0 or count_O_global > count_X_global:
			print("3")
		else:
			print("3")
		'''
	if flag_all_O > 0 and flag_all_X > 0:
#		print("meX3")
		print("3")
#	if count_O_global > count_X_global:
#		print("meX4")
#		print("3")


	'''
	Testcases
XOX
XXO
O_O

XXX
OOO
___

XOX
OX_
XO_

My cases:
XXX
O__ ---> Win(1)
O__

XOO
X__ ---> Win(1)
X__

XOO
_X_ ---> Win(1)
__X

OOO
X__ ---> Win(1)
X__

OXX
O__ ---> Win(1)
O__

OXX
_O_ ---> Win(1)
__O

XXO
OXX ---> Draw (1)
XOO 

XXO
__X ---> Reachable(2)
XOO

XXX
OOO ---> Not reachable(3)
XXX

XOX
XOX ---> Not reachable(3)
XOX 
	
XXX
OO_ ---> Not reachable(3)
O__


OXX
OO_ ---> Not reachable(3)
__O

	'''
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
