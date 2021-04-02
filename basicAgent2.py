from createMap import board
import random
import numpy as np
import math

def calculateFindingBelief(matrix, beliefState, targetLocation):

    # Belief of a cell -> P(Belief ^ Not False Negative)

    # T = potentially has target
    # F = false observation

    # B = P(Cell x = T | Cell y = F)
    # B = (P(Cell x = T) P(Cell y = F | Cell x = T)) / P(Cell y = F)

    # P(Cell y = F) = P(Cell y = F ^ Cell x = F)
    #               = P(Cell x = F) P(Cell y = F | Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T)
    #               = P(Cell x = F) (1) + P(Cell x = T) P(Cell y = F | Cell x = T)

    # Substituing this back into our initial belief equation:
    # B = (P(Cell x = T) P(Cell y = F | Cell x = T)) / (P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))

    # P(Cell y = F | Cell x = T) represents the false negative rate of the given terrain

    # Multiplying P(Not false negative) to the equation to account for NOT false negative

    # B = (P(Cell x = T) P(Cell y = F | Cell x = T)) / (P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T)) (P(Not false negative))

    # Unvisited list to keep track of which spots on the map are searching candidates
    tuples = []


    # Counter to keep track of total distance agent travels
    totalDistance = 0

    # Counter to keep track of number of searches conducted by the agent
    observedCount = 0

    # Target found boolean so we keep iterating until the target is found
    targetFound = False


    agentsBoard = matrix
    belief = beliefState

    boardDim = len(beliefState)


    for i in range(boardDim):
        for j in range(boardDim):
            belief[i,j] = float(1 / (boardDim * boardDim))
            tuples.append((i,j))

    # Initial cell agent will search
    searching = random.choice(tuples)
    tuples.remove(searching)
    

    while targetFound == False:

        previousBeliefs = belief

        currentTerrain = str(agentsBoard[searching])

        falseNegative = 0

        if currentTerrain == "f":
            falseNegative = 0.1
        elif currentTerrain == "H":
            falseNegative = 0.3
        elif currentTerrain == "F":
            falseNegative = 0.7
        elif currentTerrain == "C":
            falseNegative = 0.9


        if searching == targetLocation:
            
            num = falseNegativeCheck()

            observedCount += 1

            if num >= falseNegative:
                targetFound = True

                return observedCount, totalDistance
        else:

            observedCount += 1
        

        #(P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefNumerator = previousBeliefs[searching] * falseNegative


        #(P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefDenominator = (1 - previousBeliefs[searching]) + observingBeliefNumerator


        belief[searching] = observingBeliefNumerator / observingBeliefDenominator


        belief[searching] = (belief[searching] * (1 - falseNegative))



        beliefSum = np.sum(belief)
        belief = belief / beliefSum

        for i in range (boardDim):
            for j in range(boardDim):
                    
                if currentTerrain == "f":
                    falseNegative = 0.1
                elif currentTerrain == "H":
                    falseNegative = 0.3
                elif currentTerrain == "F":
                    falseNegative = 0.7
                elif currentTerrain == "C":
                    falseNegative = 0.9

                belief[(i,j)] = (belief[(i,j)] * (1 - falseNegative))

        beliefSum = np.sum(belief)
        #print(beliefSum)

        belief = belief / beliefSum
        #print(belief)

        maxList = largestProbabilities(belief)

        uniqueTargets = []

        for i in maxList:
            if i not in uniqueTargets:
                uniqueTargets.append(i)

        nextTarget, distanceCost = minManhattanDistance(uniqueTargets, searching)

        totalDistance += distanceCost

        uniqueList = []

        for i in nextTarget:
            if i not in uniqueList:
                uniqueList.append(i)

        if len(nextTarget) == 1:
            searching = uniqueList[0]
        else:
            searching = random.choice(uniqueList)



    return observedCount, totalDistance


def falseNegativeCheck():

    number = random.uniform(0,1)

    return number


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


def minManhattanDistance(tuples, current):

    #print(current)

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

        #print(tempMin)
        if tempMin == currMin:
            goalList.append((tempX, tempY))

        elif tempMin < currMin:
            currMin = tempMin
            goalList = []
            goalList.append((tempX, tempY))
            #print("New goals: ", goalList)

    return goalList, currMin