#empty = 0 pits = 1 wind = 2 wumpus = 3 smell = 4 gold = 5 doubt = 6 safe = 7
import random

def printmatrix(matrix, size): 
	for i in range(size):
		for j in range(size):
			print(str(matrix[i][j]), end=" ")
		print()

def matrixtostring(matrix, size):
	for i in range(size):
		for j in range(size):
			matrix[i][j] = str(matrix[i][j])
	return matrix
def initializematrix(size, number):
	return [[number for x in range(size)] for y in range(size)] 
def initialPosition(size):
	current_point_flag = True
	while(current_point_flag):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		print(str(x) + str(y))
		if(x == 0 or y == 0 or x == (size -1) or y == (size - 1)):
			current_point_flag = False

	return x, y
def game(matrix, size):
	quest_matrix = matrixtostring(initializematrix(size, -1), size)
	
	x = 0
	y = 0
	history = [[0,0]]
	game_over_flag = False
	game_result_flag = False
	
	while(not game_over_flag):
		move_flag = False
		print(str(x) + " " + str(y))
		print()
		quest_matrix[x][y] = matrix[x][y]
		
		if("5" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = True
			print("You Won the game")
		elif("3" in matrix[x][y] or "1" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = False
			print("You Lost the game")
		flagone, flagTwo, flagThree, flagFour = True, True, True, True
		directions = []
		if("0"in quest_matrix[x][y]):

			if(0 <= x-1 < (size) and "-1" in quest_matrix[x-1][y]):
				quest_matrix[x-1][y] = "7"
				
				
			if(0 <= x+1 < (size) and "-1" in quest_matrix[x+1][y]):
				quest_matrix[x+1][y] = "7"
				
				
			if(0 <= y-1 < (size) and "-1" in quest_matrix[x][y-1]):
				quest_matrix[x][y-1] = "7"
				
				
			if(0 <= y+1 < (size) and "-1" in quest_matrix[x][y+1]):
				quest_matrix[x][y+1] = "7"
			

				
		elif("2" in quest_matrix[x][y] or "4" in quest_matrix[x][y]):
			if(0 <= x-1 < (size) and "-1" in quest_matrix[x-1][y]):
				quest_matrix[x-1][y] = "6"
				
				
			if(0 <= x+1 < (size) and "-1" in quest_matrix[x+1][y]):
				quest_matrix[x+1][y] = "6"
				
			
				
			if(0 <= y-1 < (size) and "-1" in quest_matrix[x][y-1]):
				quest_matrix[x][y-1] = "6"

			if(0 <= y+1 < (size) and "-1" in quest_matrix[x][y+1]):
				quest_matrix[x][y+1] = "6"
		if(0 <= x-1 < (size) and not("6" in quest_matrix[x-1][y])):
			directions.append(1)
		if(0 <= x+1 < (size) and not("6" in quest_matrix[x+1][y])):
			directions.append(2)
		if(0 <= y-1 < (size) and not("6" in quest_matrix[x][y-1])):
			directions.append(3)
		if(0 <= y+1 < (size) and not("6" in quest_matrix[x][y+1])):
			directions.append(4)
		doubt_probility = random.uniform(0.0, 1.0)
		if(doubt_probility <= 0.2):
			directions.extend([1,2,3,4])

		printmatrix(quest_matrix, size)
		if(len(directions) > 0):
			
			move = random.choice(directions)
			if(move == 1):
				if(0 <= x-1 < (size)):
					x = x - 1
					print("Moving Top")
					move_flag = True
					history.append([x,y])
			if(move == 2):
				if(0 <= x+1 < (size)):
					x = x +1
					print("Moving Down")
					move_flag = True
					history.append([x,y])
			if(move == 3):
				if(0 <= y-1 < (size)):
					y = y-1
					print("Moving Left")
					move_flag = True
					history.append([x,y])
			if(move == 4):
				if(0 <= y+1 < (size)):
					y = y+1	
					print("Moving Right")
					move_flag = True
					history.append([x,y])


				
		
		while(not move_flag):
				print("All Sides have either smell or wind")
				print("Where to move")
				print("1. Move Top")
				print("2. Move Down")
				print("3. Move Left")
				print("4. Move Right")
				instruction = int(input(""))
				if(instruction == 1):
					if(0 <= x-1 < (size)):
						x = x-1
						print("Moving Top")
						move_flag = True
						history.append([x,y])
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 2):
					if(0 <= x+1 < (size)):
						x = x +1
						print("Moving Down")
						move_flag = True
						history.append([x,y])
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 3):
					if(0 <= y-1 < (size)):
						y = y-1
						print("Moving Left")
						move_flag = True
						history.append([x,y])
					else:
						print("Cannot move in this direction. Out of Area")
				elif(instruction == 4):
					if(0 <= y+1 < (size)):
						y = y + 1
						print("Moving Right")
						move_flag = True
						history.append([x,y])
					else:
						print("Cannot move in this direction. Out of Area")

		if("5" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = True
			
			print("Moving Back")
			for i in history:
				print(history.pop())
			print("You Won the game")

		elif("3" in matrix[x][y] or "1" in matrix[x][y]):
			game_over_flag = True
			game_result_flag = False
			print("You Lost the game")
				
		

		
		




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
	matrix = initializematrix(size, 0)
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


 

def main():
	grid_size = int(input("Enter the size of wumpus "))
	while(True):
		pits_num = int(input("Enter number of pits "))
		if(pits_num > grid_size):
			print("Pit Numbers Cannot be larger than wumpus")
		else:
			break
	wumpus = 1
	matrix = makematrix(grid_size, pits_num)
	printmatrix(matrix, grid_size)
	matrix = matrixtostring(matrix, grid_size)
	
	game(matrix, grid_size)
	#print(initialPosition(grid_size))

	
main()