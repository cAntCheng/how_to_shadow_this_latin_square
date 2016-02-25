# -*- coding: UTF-8 -*-
import random
import copy

# N = random.randint(5,7)
# latin_square = [([9]+[6]*N+[9]) for i in range(N+2)]

N = 5

latin_square = [([9]*(N+2))] + [([9]+[6]*N+[9]) for i in range(N)] + [([9]*(N+2))]

global Constraint_Numbers
Constraint_Numbers = []


# while len(Constraint_Numbers)<N/2:
# 	x = random.randint(1,N)
# 	y = random.randint(1,N)
# 	number = random.randint(0,2)
# 	if [x,y,number] not in Constraint_Numbers:
# 		Constraint_Numbers.append([x,y,number])
# 		latin_square[y][x] = number
# 	print Constraint_Numbers


Constraint_Numbers = [[1,4,2],[5,2,1]]
latin_square[1][4] = 2
latin_square[5][2] = 1

for constraint_number in Constraint_Numbers:
	if constraint_number[2] == 0:
		x = constraint_number[0]
		y = constraint_number[1]
		latin_square[y-1][x-1] = 9
		latin_square[y-1][x] = 9
		latin_square[y-1][x+1] = 9
		latin_square[y][x-1] = 9
		latin_square[y][x+1] = 9
		latin_square[y+1][x-1] = 9
		latin_square[y+1][x] = 9
		latin_square[y+1][x+1] = 9

def checkNumbersAroundCurrentGrid():
	pass

def getAroundGridsValue(latin_square,row,i):
	return [latin_square[row-1][i-1],latin_square[row-1][i], latin_square[row-1][i+1],
			latin_square[row][i-1], latin_square[row][i+1],
			latin_square[row+1][i-1], latin_square[row+1][i], latin_square[row+1][i+1],
			]
			
def getAroundGrids(latin_square,row,i):
	return [[row-1,i-1,latin_square[row-1][i-1]], [row-1,i,latin_square[row-1][i]], [row-1,i+1,latin_square[row-1][i+1]],
			[row,i-1,latin_square[row][i-1]], [row,i+1,latin_square[row][i+1]],
			[row+1,i-1,latin_square[row+1][i-1]], [row+1,i,latin_square[row+1][i]], [row+1,i+1,latin_square[row+1][i+1]],
			]

def checkShadowsAroundNumberGrid(one,latin_square):
	one_y = one[0]
	one_x = one[1]
	# 此处可能可以优化，通过判断one和当前要涂黑格子的位置，减少around_one列表内格子数量
	grids_around_one = getAroundGridsValue(latin_square, one_y, one_x)
	around_one_count = 0
	for grid_around_one in grids_around_one:
		if grid_around_one == 8:
			around_one_count += 1
	return one[2] == around_one_count




def printSquare(latin_square):
	global Constraint_Numbers
	for i in range(1,N+1):
		if 8 not in latin_square[i]:
			return
	for one in Constraint_Numbers:
		if not checkShadowsAroundNumberGrid(one,latin_square):
			return

	print "begin"
	for row in latin_square:
		for i in row:
			print i,
		print "\n"
	else:
		print "end"

def solve(row, which, latin_square, N):
	for i in range(1,N+1):
		if latin_square[row][i] not in [0,1,2]:
			latin_square[row][i] = 9
		if latin_square[i][which] not in [0,1,2]:
			latin_square[i][which] = 9
		if latin_square[row][i] == 8:
			return
		if latin_square[i][which] == 8:
			return
	latin_square[row][which] = 8
	print "row:",row,"which:",which

	if row == N:
		printSquare(latin_square)
	else:
		for i in range(1,N+1):
			if latin_square[row+1][i] in [0,1,2,9]:
				continue

			around = getAroundGrids(latin_square, row+1, i)
			flag_has_constraint_number = 0
			flag_end = 0
			around_one_counts = []
			for one in around:
				flag_end += 1
				if one[2] in [1,2]:
					flag_has_constraint_number += 1
					one_y = one[0]
					one_x = one[1]
					if not checkShadowsAroundNumberGrid(one, latin_square):
						solve(row+1,i,copy.deepcopy(latin_square), N)
				if flag_end == len(around) and flag_has_constraint_number == 0:
					solve(row+1,i,copy.deepcopy(latin_square), N)



for x in range(1,N+1):
	y = 1
	print "x=",x,"y=",y
	solve(y,x,copy.deepcopy(latin_square), N)
else:
	print "jieshu"






