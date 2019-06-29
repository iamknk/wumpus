#empty = 0 pits = 1 wind = 2 wumpus = 3 smell = 4
import random
def windorsmell(matrix, x, y, size, windorsmell):
	if(windorsmell == 2):
		if(x-1 < (size ) and matrix[x-1][y] != (1 or 3)):
			matrix[x-1][y] = windorsmell
		if(x+1 < (size) and matrix[x+1][y] != (1 or 3)):
			matrix[x+1][y] = windorsmell
		if(y-1 < (size) and matrix[x][y-1] != (1 or 3)):
			matrix[x][y-1] = windorsmell
		if(y+1 < (size) and matrix[x][y+1] != (1 or 3)):
			matrix[x][y+1] = windorsmell
	if(windorsmell == 4):
		if(x-1 < (size ) and matrix[x-1][y] != (1 or 3)):
			matrix[x-1][y] = int(str(matrix[x-1][y]) + "4")
		if(x+1 < (size) and matrix[x+1][y] != (1 or 3)):
			matrix[x+1][y] = int(str(matrix[x+1][y]) + "4")
		if(y-1 < (size) and matrix[x][y-1] != (1 or 3)):
			matrix[x][y-1] = int(str(matrix[x][y-1]) + "4")
		if(y+1 < (size) and matrix[x][y+1] != (1 or 3)):
			matrix[x][y+1] = int(str(matrix[x][y+1]) +  "4")



def makematrix(size, pits):
	matrix = [[0 for x in range(size)] for y in range(size)] 
	for i in range(pits):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		matrix[x][y] = 1
		
		windorsmell(matrix, x, y, size, 2)
	wumpus_flag = True
	x = random.randint(0, size-1)
	y = random.randint(0, size-1)
	while(wumpus_flag):
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
	printmatrix(matrix, wumpus_size)
	
main()