
import random

mx = 8 
my = 8 # width and height of the maze
maze = [[0 for x in range(mx)] for y in range(my)]
verWall = [[1 for x in range(mx+1)] for y in range(my+1)]
horWall = [[1 for x in range(mx+1)] for y in range(my+1)]
possibleDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
color = [0, 1] # RGB colors of the maze

def printMaze():
    mazePrintable = [[] for y in range(my*3)]
    for x in range(mx):
        for y in range(my):
            mazePrintable[x*2].append("XX")
            if horWall[x][y]:
                mazePrintable[x*2].append("XX")
            else:
                mazePrintable[x*2].append("  ")
            if verWall[x][y]:
                mazePrintable[x*2+1].append("XX")
            else:
                mazePrintable[x*2+1].append("  ")
            mazePrintable[x*2+1].append("  ")

    for x in range(mx):
        mazePrintable[x*2].append("XX")
        mazePrintable[x*2+1].append("XX")
    for y in range(my):
        mazePrintable[mx*2].append("XXXX")
    mazePrintable[mx*2].append("XX")

    for i in mazePrintable:
        if not len(i):
            continue
        for j in i:
            print(j,end='')
        print()
    print()

def generateMaze(x,y):
    #print(x,y)
    #printMaze()
    maze[x][y] = 1
    visitOrder = possibleDirections[:]
    random.shuffle(visitOrder)
    for direction in visitOrder:
        dx = x+direction[0]
        dy = y+direction[1]
        if dx<0 or dx>=mx or dy<0 or dy>=my:
            continue
        if maze[dx][dy] == 0:
            if direction[1] == 1:
                verWall[dx][dy] = 0
            if direction[1] == -1:
                verWall[dx][dy+1] = 0
            if direction[0] == 1:
                horWall[dx][dy] = 0
            if direction[0] == -1:
                horWall[dx+1][dy] = 0
            generateMaze(dx,dy)

generateMaze(random.randint(0, mx - 1), random.randint(0, my - 1))
#generateMaze(1, 1)

for i in range(random.randint(10, 20)):
    horWall[random.randint(1, mx-1)][random.randint(1, mx-1)] = 0
for i in range(random.randint(10, 20)):
    verWall[random.randint(1, mx-1)][random.randint(1, mx-1)] = 0
    

printMaze()
