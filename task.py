#empty = 0 pits = 1 wind = 2 wumpus = 3 smell = 4 gold = 5
import random
def game(matrix, size):
	current_point_flag = True
	while(current_point_flag):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		if(x == 0 or y == 0 or x == (size -1) or y == (size - 1)):
			current_point_flag = False

	current_point = [x,y]
	game_over_flag = False
	game_result_flag = False
	if("5" in matrix[x][y]):
		game_over_flag = True
		game_result_flag = True

	while(not game_over_flag):
		print(current_point)
		move_flag = False
		if("5" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = True
			move_flag = True
		
		flagone, flagTwo, flagThree, flagFour = True, True, True, True
		if("1" in matrix[x][y] or "3" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = False
		if(0 <= x-1 < (size) and (not move_flag)):
			if("2" in matrix[x-1][y] or "4" in matrix[x-1][y]):
				flagone = False
		if(0 <= x+1 < (size) and (not move_flag)):
			if("2" in matrix[x+1][y] or "4" in matrix[x+1][y]):
				flagTwo = False
		if(0 <= y-1 < (size) and (not move_flag)):
			if("2" in matrix[x][y-1] or "4" in matrix[x][y-1]):
				flagThree = False
		if(0 <= y+1 < (size) and (not move_flag)):
			if("2" in matrix[x][y+1] or "4" in matrix[x][y+1]):
				flagFour = False
		if(flagone or flagTwo or flagThree or flagFour):
			if(0 <= x-1 < (size)):
				if(flagone):
					current_point = [x-1,y]
					move_flag = True
			if(0 <= x+1 < (size)):
				if(flagTwo):
					current_point = [x+1,y]
					move_flag = True
			if(0 <= y-1 < (size)):
				if(flagThree):
					current_point = [x, y-1]
					move_flag = True
			if(0 <= y+1 < (size)):
				if(flagFour):
					current_point = [x, y+1]
					move_flag = True
		else:
			while(not move_flag):
				print("All Sides have either smell or wind")
				print("Where to move")
				print("1. Move Left")
				print("2. Move Right")
				print("3. Move Up")
				print("4. Move Down")
				instruction = int(input(""))
				if(instruction == 1):
					if(0 <= x-1 < (size)):
						current_point = [x-1, y]
						move_flag = True
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 2):
					if(0 <= x+1 < (size)):
						current_point = [x+1, y]
						move_flag = True
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 3):
					if(0 <= y-1 < (size)):
						current_point = [x, y-1]
						move_flag = True
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 2):
					if(0 <= y+1 < (size)):
						current_point = [x, y+1]
						move_flag = True
					else:
						print("Cannot move in this direction. Out of Area")



				
		#game_over_flag = True

	if(game_result_flag == True):
		print("You Won the Game")
	else:
		print("You Lost the Game")



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
			
def matrixtostring(matrix, size):
	for i in range(size):
		for j in range(size):
			matrix[i][j] = str(matrix[i][j])
	return matrix


def makematrix(size, pits):
	matrix = [[0 for x in range(size)] for y in range(size)] 
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
			print(str(i) + "X" + str(j))
			print(matrix[i][j])
 

def main():
	wumpus_size = int(input("Enter the size of wumpus "))
	pits_num = int(input("Enter number of pits "))
	wumpus = 1
	matrix = makematrix(wumpus_size, pits_num)
	#printmatrix(matrix, wumpus_size)
	matrix = matrixtostring(matrix, wumpus_size)
	
	game(matrix, wumpus_size)

	
main()