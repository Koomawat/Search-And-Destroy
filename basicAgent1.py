from createMap import board
import random
import numpy as np
import math

def calculateBelief(matrix, beliefState, targetLocation):

    

    # Belief of a cell 

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


    # Unvisited list to keep track of which spots on the map are searching candidates
    tuples = []

    # Observed list to keep track of which cells of the map have been searched
    observed = []

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
    
    #while targetFound == False:
    for i in range(3):
    #if 1 == 1:

        print("Searching at: ", searching)

        previousBeliefs = belief

        currentTerrain = str(agentsBoard[searching])
        #print(currentTerrain)

        falseNegative = 0


        if currentTerrain == "f":
            falseNegative = 0.1
        elif currentTerrain == "H":
            falseNegative = 0.3
        elif currentTerrain == "C":
            falseNegative = 0.9
        else:
            falseNegative = 0.7


        if searching == targetLocation:

            num = falseNegativeCheck()

            if num > falseNegative:
                print("Target Found!")
                return agentsBoard
        

        #(P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefNumerator = previousBeliefs[searching] * falseNegative
        #print(observingBeliefNumerator)

        #(P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefDenominator = (1 - previousBeliefs[searching]) + observingBeliefNumerator
        #print(observingBeliefDenominator)

        belief[searching] = observingBeliefNumerator / observingBeliefDenominator
        #print("Belief: ", belief)

        observed.append(searching)
        #print(observed)

        for i in range (boardDim):
            for j in range(boardDim):
                if (i,j) not in observed:
                    beliefNumerator = previousBeliefs[(i,j)]
                    #print(beliefNumerator)
                    #print(beliefDenominator)
                    belief[(i,j)] = beliefNumerator / observingBeliefDenominator

        #print(np.sum(belief))

        print("Current belief: ")
        print(belief)

        observed = []
        #searching = random.choice(tuples)

        maxList = largestProbabilities(belief)

        uniqueTargets = []

        for i in maxList:
            if i not in uniqueTargets:
                uniqueTargets.append(i)

        print("Max list: ", uniqueTargets)    

        nextTarget, distanceCost = minManhattanDistance(uniqueTargets, searching)

        if len(nextTarget) == 1:
            searching = nextTarget[0]
        else:
            searching = random.choice(nextTarget)

        uniqueList = []

        for i in nextTarget:
            if i not in uniqueList:
                uniqueList.append(i)

        print("Next possible: ", uniqueList)
        print()
        #print(distanceCost)

        #return

    return belief


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

    print(current)

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