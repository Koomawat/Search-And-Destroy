import numpy as np
import random
import copy
from collections import deque

from numpy.core.defchararray import add

def main():

    np.set_printoptions(precision=4)

    testBoard = np.zeros((3,3),dtype=np.float64)

    visiting = []

    print(testBoard)

    for i in range(3):
        for j in range(3):
            testBoard[i,j] = 1/9
            visiting.append((i,j))
            
    print(testBoard)

    mlen = len(testBoard)
    ans = bfs(testBoard, (mlen-1,mlen-1), (0,0), mlen)
    print(ans)
    listA = traversePath(ans, testBoard, 2, 2)
    print(listA)
    return

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

if __name__ == "__main__":
    main()