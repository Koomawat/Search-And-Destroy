import numpy as np
import random

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