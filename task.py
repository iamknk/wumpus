#empty = 0 pits = 1 wind = 2 wumpus = 3 smell = 4 gold = 5 doubt = 6 safe = 7
import random
# def game(matrix, size):
# 	current_point_flag = True
# 	while(current_point_flag):
# 		x = random.randint(0, size-1)
# 		y = random.randint(0, size-1)
# 		if(x == 0 or y == 0 or x == (size -1) or y == (size - 1) and ("1" in matrix[x][y] and "3" in matrix[x][y])):
# 			current_point_flag = False

# 	current_point = [x,y]
# 	game_over_flag = False
# 	game_result_flag = False
# 	if("5" in matrix[x][y]):
# 		game_over_flag = True
# 		game_result_flag = True


# 	while(not game_over_flag):
# 		current_point = [x,y]
# 		print(current_point)
# 		move_flag = False
# 		if("5" in matrix[x][y]):
# 			game_over_flag = True
# 			game_result_flag = True
# 			move_flag = True
# 			break 
# 		if("1" in matrix[x][y] or "3" in matrix[x][y]):
# 			game_over_flag = True
# 			game_result_flag = False
# 			move_flag = True
# 			break

		
# 		flagone, flagTwo, flagThree, flagFour = True, True, True, True
# 		if(0 <= x-1 < (size) and (not move_flag)):
# 			if("2" in matrix[x-1][y] or "4" in matrix[x-1][y]):
# 				flagone = False
# 		if(0 <= x+1 < (size) and (not move_flag)):
# 			if("2" in matrix[x+1][y] or "4" in matrix[x+1][y]):
# 				flagTwo = False
# 		if(0 <= y-1 < (size) and (not move_flag)):
# 			if("2" in matrix[x][y-1] or "4" in matrix[x][y-1]):
# 				flagThree = False
# 		if(0 <= y+1 < (size) and (not move_flag)):
# 			if("2" in matrix[x][y+1] or "4" in matrix[x][y+1]):
# 				flagFour = False
# 		if(flagone or flagTwo or flagThree or flagFour):
# 			if(0 <= x-1 < (size)):
# 				if(flagone):
# 					x = x-1
# 					#current_point = [x-1,y]
# 					move_flag = True
# 			elif(0 <= x+1 < (size)):
# 				if(flagTwo):
# 					x = x+1
# 					#current_point = [x+1,y]
# 					move_flag = True
# 			elif(0 <= y-1 < (size)):
# 				if(flagThree):
# 					y = y-1
# 					#current_point = [x, y-1]
# 					move_flag = True
# 			elif(0 <= y+1 < (size)):
# 				if(flagFour):
# 					y = y + 1
# 					#current_point = [x, y+1]
# 					move_flag = True
# 		else:
# 			while(not move_flag):
# 				print("All Sides have either smell or wind")
# 				print("Where to move")
# 				print("1. Move Left")
# 				print("2. Move Right")
# 				print("3. Move Up")
# 				print("4. Move Down")
# 				instruction = int(input(""))
# 				if(instruction == 1):
# 					if(0 <= x-1 < (size)):
# 						x = x-1
# 						#current_point = [x-1, y]
# 						move_flag = True
# 					else:
# 						print("Cannot move in this direction. Out of Area")
# 				elif(instruction == 2):
# 					if(0 <= x+1 < (size)):
# 						x = x +1
# 						#current_point = [x+1, y]
# 						move_flag = True
# 					else:
# 						print("Cannot move in this direction. Out of Area")
# 				elif(instruction == 3):
# 					if(0 <= y-1 < (size)):
# 						y = y-1
# 						#current_point = [x, y-1]
# 						move_flag = True
# 					else:
# 						print("Cannot move in this direction. Out of Area")
# 				elif(instruction == 2):
# 					if(0 <= y+1 < (size)):
# 						y = y + 1
# 						#current_point = [x, y+1]
# 						move_flag = True
# 					else:
# 						print("Cannot move in this direction. Out of Area")



				
		
		

# 	if(game_result_flag == True):
# 		print("You Won the Game")
# 	else:
# 		print("You Lost the Game")
def matrixtostring(matrix, size):
	for i in range(size):
		for j in range(size):
			matrix[i][j] = str(matrix[i][j])
	return matrix
def initializematrix(size):
	return [[-1 for x in range(size)] for y in range(size)] 
def game(matrix, size):
	quest_matrix = matrixtostring(initializematrix(size))
	print(quest_matrix)
	current_point_flag = True
	while(current_point_flag):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		if(x == 0 or y == 0 or x == (size -1) or y == (size - 1) and ("1" in matrix[x][y] and "3" in matrix[x][y])):
			current_point_flag = False

	current_point = [x,y]
	game_over_flag = False
	game_result_flag = False
	if("5" in matrix[x][y]):
		game_over_flag = True
		game_result_flag = True
	while(not game_over_flag):
		quest_matrix[x][y] = matrix[x][y]
		if("0"in quest_matrix[x][y]):
			flagone, flagTwo, flagThree, flagFour = True, True, True, True
			if(0 <= x-1 < (size)):
				quest_matrix[x-1][y] = "7"
			elif(0 <= x+1 < (size)):
				quest_matrix[x+1][y] = "7"
			elif(0 <= y-1 < (size)):
				quest_matrix[x][y-1] = "7"
			elif(0 <= y+1 < (size)):
				quest_matrix[x][y+1] = "7"
		elif("2" in quest_matrix[x][y] or "4" in quest_matrix[x][y]):
			flagone, flagTwo, flagThree, flagFour = False, False, False, False
		if(0 <= x-1 < (size)):
			if(flagone and not move_flag):
				x = x-1
				move_flag = True
			else:
				if("-1" in quest_matrix[x-1][y]):
					quest_matrix[x-1][y] = "6"

		if(0 <= x+1 < (size)):
			if(flagTwo and not move_flag):
				x = x+1
				move_flag = True
			else:
				if("-1" in quest_matrix[x-1][y]):
					quest_matrix[x+1][y] = "6"
		if(0 <= y-1 < (size)):
			if(flagThree and not move_flag):
				y = y-1
				move_flag = True
			else:
				if("-1" in quest_matrix[x-1][y]):
					quest_matrix[x][y-1] = "6"
		if(0 <= y+1 < (size)):
			if(flagFour and not move_flag):
				y = y + 1
				move_flag = True
			else:
				if("-1" in quest_matrix[x-1][y]):
					quest_matrix[x][y+1] = "6"
		if(0 <= x-1 < (size) and not move_flag):
			if("0" in quest_matrix[x-1][y] or "5" in quest_matrix[x-1][y]):

		elif(0 <= x+1 < (size)):
			if(flagTwo):
				x = x+1
				move_flag = True
		elif(0 <= y-1 < (size)):
			if(flagThree):
				y = y-1
				#current_point = [x, y-1]
				move_flag = True
		elif(0 <= y+1 < (size)):
			if(flagFour):
				y = y + 1
				#current_point = [x, y+1]
				move_flag = True

		
		




def windorsmell(matrix, x, y, size, windorsmell):
	if(windorsmell == 2):
		if(0 <= x-1 < (size) and matrix[x-1][y] != (1 or 3)):
			matrix[x-1][y] = windorsmell
		if(0 <= x+1 < (size) and matrix[x+1][y] != (1 or 3)):
			matrix[x+1][y] = windorsmell
		if(0 <= y-1 < (size) and matrix[x][y-1] != (1 or 3)):
			matrix[x][y-1] = windorsmell
		if(0 <= y+1 < (size) and matrix[x][y+1] != (1 or 3)):
			matrix[x][y+1] = windorsmell
	if(windorsmell == 4):
		if(0 <= x-1 < (size ) and matrix[x-1][y] != (1 or 3)):
			matrix[x-1][y] = int(str(matrix[x-1][y]) + "4")
		if(0 <= x+1 < (size) and matrix[x+1][y] != (1 or 3)):
			matrix[x+1][y] = int(str(matrix[x+1][y]) + "4")
		if(0 <= y-1 < (size) and matrix[x][y-1] != (1 or 3)):
			matrix[x][y-1] = int(str(matrix[x][y-1]) + "4")
		if(0 <= y+1 < (size) and matrix[x][y+1] != (1 or 3)):
			matrix[x][y+1] = int(str(matrix[x][y+1]) +  "4")
	return matrix
			



def makematrix(size, pits):
	matrix = initializematrix(size)
	for i in range(pits):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		matrix[x][y] = 1
		
		matrix = windorsmell(matrix, x, y, size, 2)
	wumpus_flag = True
	
	while(wumpus_flag):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		print(type(matrix[x][y]))
		if(matrix[x][y] != 0):
			if(matrix[x][y] == 2):
				matrix[x][y] = str(matrix[x][y]) + "3"
				matrix[x][y] = int(matrix[x][y])
				wumpus_flag = False
				windorsmell(matrix, x, y, size, 4)

		else:
			matrix[x][y] = 3
			wumpus_flag = False
			windorsmell(matrix, x, y, size, 4)
		gold_flag = True
		while(gold_flag):
			x = random.randint(0, size-1)
			y = random.randint(0, size-1)
			if(isinstance(matrix[x][y], int)):
				if(matrix[x][y] == 0):
					matrix[x][y] = 5
					gold_flag = False

	return matrix

def printmatrix(matrix, size): 
	for i in range(size):
		for j in range(size):
			print(str(i) + "X" + str(j) + " = " + str(matrix[i][j]))
			print()
 

def main():
	wumpus_size = int(input("Enter the size of wumpus "))
	while(True):
		pits_num = int(input("Enter number of pits "))
		if(pits_num > wumpus_size):
			print("Pit Numbers Cannot be larger than wumpus")
		else:
			break
	wumpus = 1
	matrix = makematrix(wumpus_size, pits_num)
	printmatrix(matrix, wumpus_size)
	matrix = matrixtostring(matrix, wumpus_size)
	
	game(matrix, wumpus_size)

	
main()