import numpy as np
import random
import copy
from collections import deque

# Board for terrain
def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard


# Board for agent
def agentBoard(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=np.float64)

    return gameboard


# Generating terrain
def makeTerrain(terrainMap):

    # Possible Terrain Choices

    terrainChoices = ["Flat", "Hilly", "Forested", "Caves"]

    # Randomly setting a cell to a terrain type with each terrain having 1/4 chance

    for i in range(len(terrainMap)):
        for j in range(len(terrainMap)):

            terrianType = random.choice(terrainChoices)

            # 'f' designates Flat

            if(terrianType == "Flat"):
                terrainMap[i,j] = 'f'

            # 'H' designates Hilly

            elif (terrianType == "Hilly"):
                terrainMap[i,j] = 'H'

            # 'F' designates Forest

            elif (terrianType == "Forested"):
                terrainMap[i,j] = 'F'

            # 'C' designates Caves

            else:
                terrainMap[i,j] = 'C'

    lenTerrain = len(terrainMap)
    randX = random.randint(0,lenTerrain-1)
    randY = random.randint(0,lenTerrain-1)
    targetLocation = (randX, randY)

    return terrainMap, targetLocation


# False negative function check
def falseNegativeCheck():

    number = random.uniform(0,1)

    return number


# Finding the largest probabilities in the agent's belief state
def largestProbabilities(belief):

    
    maxList = []

    maxVal = belief[0,0]
    maxList.append((0,0))

    for i in range(len(belief)):
        for j in range(len(belief)):

            curr = belief[i,j]
            if curr == maxVal:
                maxList.append((i,j))
            elif curr > maxVal:
                maxVal = belief[i,j]
                maxList = []
                maxList.append((i,j))

    return maxList


# Calculating the minimum manhattan distance between the largest equal probabilities 
def minManhattanDistance(tuples, current):

    currX = current[0]
    currY = current[1]
    
    nextSearchTarget = tuples[0]

    currMinX = nextSearchTarget[0]
    currMinY = nextSearchTarget[1]

    currMin = abs(currMinX - currX) + abs(currMinY - currY)

    tuples.remove((tuples[0]))

    goalList = []
    goalList.append((currMinX, currMinY))

    lenTuples = len(tuples)

    for i in range(lenTuples):

        tempX = tuples[i][0]
        tempY = tuples[i][1]

        tempMin = abs(tempX - currX) + abs(tempY - currY)

        if tempMin == currMin:
            goalList.append((tempX, tempY))

        elif tempMin < currMin:
            currMin = tempMin
            goalList = []
            goalList.append((tempX, tempY))

    return goalList, currMin


def bfs(main_maze, start, goal, mlen):

    maze = copy.deepcopy(main_maze)

    # Initialize the queue and set the start and empty path string
    queue = deque([[start, ""]])

    # create a visited set (can do with list too) 
    visited = set()

    # Convert the 2D array into a dictionary
    tree = arrayToTree(maze)

    while queue:

        tuples = (values) = queue.popleft()
        node, path = tuples

        (x, y) = node
        # if the goal is found, return the path
        if node == goal:
            return path #, len(visited) # the number of nodes explored by BFS

        # keep getting an out of bounds axis error
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue

         # if the node is empty and hasnt been visited yet, add its neighbours to the queue
        elif maze[x, y] < 1 and node not in visited:
            visited.add(node)
            for movement, neighborElements in tree[node]:
                # path = current path + new movement, doing it outside the append broke it randomly
                queue.append((neighborElements, path + movement))

    # if no path is found
    return "No such path from S to G exists" #, int(len(visited)) # for number of nodes explored by BFS


def arrayToTree(maze):
    
    # Converting a 2D numpy matrix into a "tree" like structure in using dictionaries
    dim = len(maze)

    # Setting the key of the dictionary to be the element location in the matrix
    tree = {(x, y): 
    # Values only set for elements where there is a free cell 
    # Occupied cells (represented by 1) and fire cells (represented by 2) are ignored
    # 4 represents a future fire state
    []  for y in range(dim) 
            for x in range(dim)}

    # Calling the neighbor function to set 
    
    return setNeighbors(tree,maze)


def setNeighbors(tree,maze):

    dim = len(maze)

    # Traversing for each key (or in other words 2d array element) in the tree dictionary and checking valid neighbors
    for x, y in tree.keys():
        
        # Neighbors can only be Down(D) or Right(R) if x,y is top left corner
        if(x == 0 and y == 0):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Up(U) or Right(R) if x,y is bottom left corner
        elif(x == (dim - 1) and y == 0):

                tree[(x, y)].append(("U", (x - 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Down(U) or Left(L) if x,y is top right corner
        elif(x == 0 and y == (dim - 1)):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U) or Left(L) if x,y is bottom right corner
        elif(x == (dim - 1) and y == (dim - 1)):

                tree[(x, y)].append(("U", (x - 1, y)))
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Left(L) on the upper edge
        elif(x == 0 and y != (0) and (y < (dim - 1))):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U), Right(R) or Left(L) on the bottom edge
        elif(x == (dim - 1) and y != (0) and (y < (dim - 1))):

                tree[(x, y)].append(("U", (x - 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Up(U) on the left edge 
        elif(y == 0 and x != (0) and (x < (dim - 1))):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))
                tree[(x, y)].append(("U", (x-1, y)))

        # Neighbors can only be Down(D), Left(L) or Up(U) on the right edge 
        elif(y == (dim - 1) and x != (0) and (x < (dim - 1))):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("L", (x, y - 1)))
                tree[(x, y)].append(("U", (x - 1, y)))

        # Neighbors can be Down(D), Right(R), Left(L), or Up(U) on not edges
        elif(x != (0) and (x < (dim - 1)) and y != (0) and (y < (dim - 1))):

                tree[(x, y)].append(("D", (x + 1, y)))
                tree[(x, y)].append(("R", (x, y + 1)))
                tree[(x, y)].append(("L", (x, y - 1)))
                tree[(x, y)].append(("U", (x - 1, y)))

    return tree


def traversePath(path, main_maze, y, x): 
    
    maze = copy.deepcopy(main_maze)
    spread_maze = maze

    mlen = len(spread_maze)
    
    # check bounds
    if x >= mlen or y >= mlen or x < 0 or y < 0:
        return "outie"

    pathList = []
    # for each direction in the path
    for letter in path:
        # spread the fire for each movement

        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue
        elif letter == "R":
            x += 1
            pathList.append((x,y))
        elif letter == "L":
            x -= 1
            pathList.append((x,y))
        elif letter == "U":
            y -= 1
            pathList.append((x,y))
        elif letter == "D":
            y += 1
            pathList.append((x,y))
        # [row, col] since parameters are in y, x


    return pathList


def moveTarget(currentTarget, dim):

    moveChoices = ["U", "D", "L", "R"]

    movement = random.choice(moveChoices)

    nextTarget = currentTarget

    x = currentTarget[0]
    y = currentTarget[1]

    retry = True

    while retry == True:

        if(movement == "U"):
            if x-1 >= 0:
                nextTarget = (x-1, y)
                retry = False
            else: 
                moveChoices.remove("U")
                movement = random.choice(moveChoices)

        elif (movement == "D"):
            if x+1 < dim:
                nextTarget = (x+1, y)
                retry = False
            else: 
                moveChoices.remove("D")
                movement = random.choice(moveChoices)

        elif (movement == "L"):
            if y-1 >= 0:
                nextTarget = (x, y-1)
                retry = False
            else: 
                moveChoices.remove("L")
                movement = random.choice(moveChoices)

        else:
            if y+1 < dim:
                nextTarget = (x, y+1)
                retry = False
            else: 
                moveChoices.remove("R")
                movement = random.choice(moveChoices)

    return nextTarget


def manhattan5Search(belief, currentlyAt):

    manhattanCandidates = []
    currentX = currentlyAt[0]
    currentY = currentlyAt[1]

    for i in range(len(belief)):
        for j in range(len(belief)):
            
            distance = abs(currentX - i) + abs(currentY - j)

            if distance <= 5:
                manhattanCandidates.append((i,j))

    return manhattanCandidates


def movementUpdates(belief):

    originalBelief = belief

    lenBelief = len(belief)

    for i in range(lenBelief):
        for j in range(lenBelief):

            #top left
            if i == 0 and j == 0:

                belief[i,j] = (originalBelief[0,1] * (1/3)) + (originalBelief[1,0] * (1/3))

            #bot left
            elif i == lenBelief-1 and j == 0:

                belief[i,j] = (originalBelief[i-1,0] * (1/3)) + (originalBelief[i,j+1] * (1/3))

            #top right
            elif i == 0 and j == lenBelief-1:

                belief[i,j] = (originalBelief[i,j-1] * (1/3)) + (originalBelief[i+1,j] * (1/3))

            #bot right
            elif i == lenBelief-1 and j == lenBelief-1:

                belief[i,j] = (originalBelief[i-1,j] * (1/3)) + (originalBelief[i,j-1] * (1/3))
            

            #if (0,len-2)
            elif i == 0 and j == lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/2)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3))

            #if (0,1)
            elif i == 0 and j == 1:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/2))

            #if (1,1)
            elif i == 1 and j == 1:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3)) + (originalBelief[i-1,j] * (1/3))

            #if (1,len-2)
            elif i == 1 and j == lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3)) + (originalBelief[i-1,j] * (1/3))


            #if (1,0)
            elif i == 1 and j == 0:

                belief[i,j] = (originalBelief[i-1,j] * (1/2)) + (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/3))

            #if (len-2,0)
            elif i == lenBelief-2 and j == 0:

                belief[i,j] = (originalBelief[i-1,j] * (1/3)) + (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/2))

            #if (1, len-1)
            elif i == 1 and j == lenBelief-1:

                belief[i,j] = (originalBelief[i-1,j] * (1/2)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i+1,j] * (1/3))

            #if (len-2, len-1)
            elif i == lenBelief-2 and j == lenBelief-1:

                belief[i,j] = (originalBelief[i-1,j] * (1/3)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i+1,j] * (1/2))

            #if (len-1, 1)
            elif i == lenBelief-1 and j == 1:

                belief[i,j] = (originalBelief[i,j+1] * (1/2)) + (originalBelief[i-1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3))

            #if (len-1, len-2)
            elif i == lenBelief-1 and j == lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i-1,j] * (1/4)) + (originalBelief[i,j-1] * (1/2))

            #if (len-2,1)
            elif i == lenBelief-2 and j == 1:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/3)) + (originalBelief[i,j-1] * (1/3)) + (originalBelief[i-1,j] * (1/4))

            #if (len-2,len-2)
            elif i == lenBelief and j == lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i+1,j] * (1/3)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i-1,j] * (1/4))

            #top edge
            elif i == 0 and j != 0 and j != lenBelief-1 and j != 1 and j != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3))

            #left edge
            elif i != 0 and i != lenBelief-1 and j == 0 and i != 1 and i != lenBelief-2:

                belief[i,j] = (originalBelief[i-1,j] * (1/3)) + (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/3))

            #right edge
            elif i != 0 and i != 1 and i != lenBelief-1 and i != lenBelief-2 and j == lenBelief-1 :

                belief[i,j] = (originalBelief[i-1,j] * (1/3)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i+1,j] * (1/3))

            #bot edge
            elif i == lenBelief-1 and j != 0 and j != 1 and j != lenBelief-1 and j != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i-1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3))

            #if 2nd top row 
            elif i == 1 and j != 0 and j != 1 and j != lenBelief-1 and j != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i-1,j] * (1/3))

            #if 2nd left col
            elif j == 1 and i != 0 and i != 1 and i != lenBelief-1 and i != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/3)) + (originalBelief[i-1,j] * (1/4))

            #if 2nd right row 
            elif j == lenBelief-2 and i != 0 and i != 1 and i != lenBelief-1 and i != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/3)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i-1,j] * (1/4))

            #if 2nd bot row 
            elif i == lenBelief-2 and j != 0 and j != 1 and j != lenBelief-1 and j != lenBelief-2:

                belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i+1,j] * (1/3)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i-1,j] * (1/4))

            else:   
               
               belief[i,j] = (originalBelief[i,j+1] * (1/4)) + (originalBelief[i,j-1] * (1/4)) + (originalBelief[i+1,j] * (1/4)) + (originalBelief[i-1,j] * (1/4))

    return belief