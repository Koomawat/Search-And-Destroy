from mapFunctions import *
import random
import numpy as np

def calculateContainingBelief(matrix, beliefState, targetLocation, initialLocation):

    # Belief of a cell -> P(Belief)

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


    # # Unvisited list to keep track of which spots on the map are searching candidates
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

    # Calculating initial belief state of agent where each cell has an equal probability
    for i in range(boardDim):
        for j in range(boardDim):
            belief[i,j] = float(1 / (boardDim * boardDim))
            tuples.append((i,j))

    # # Initial cell agent will search
    # searching = random.choice(tuples)
    searching = initialLocation
    
    # Keeping iterating until the target is found and returned
    while targetFound == False:

        # Keeping track of previous belief, used for updating later
        previousBeliefs = belief

        currentTerrain = str(agentsBoard[searching])

        falseNegative = 0

        # False negative values of terrains
        if currentTerrain == "f":
            falseNegative = 0.1
        elif currentTerrain == "H":
            falseNegative = 0.3
        elif currentTerrain == "F":
            falseNegative = 0.7
        elif currentTerrain == "C":
            falseNegative = 0.9

        # If current location is where the target is: do a false negative check
        # Random number from 0 to 1 is generated, if it is greater than the terrain type's false negative that means the target has been found
        if searching == targetLocation:
            
            num = falseNegativeCheck()

            observedCount += 1

            if num >= falseNegative:
                targetFound = True

                return observedCount, totalDistance
        else:

            observedCount += 1
        

        # (P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefNumerator = previousBeliefs[searching] * falseNegative

        # (P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefDenominator = (1 - previousBeliefs[searching]) + observingBeliefNumerator

        # (P(Cell x = T) P(Cell y = F | Cell x = T)) / (P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))
        belief[searching] = observingBeliefNumerator / observingBeliefDenominator

        # Normalizing the rest of the belief state
        beliefSum = np.sum(belief)
        belief = belief / beliefSum

        # Finding the tuples of the largest probabilities 
        maxList = largestProbabilities(belief)

        uniqueTargets = []

        # Removing duplicates in max probability list
        for i in maxList:
            if i not in uniqueTargets:
                uniqueTargets.append(i)

        # Seeking the next target to search and calculating the cost to do so
        nextTarget, distanceCost = minManhattanDistance(uniqueTargets, searching)

        totalDistance += distanceCost

        uniqueList = []

        for i in nextTarget:
            if i not in uniqueList:
                uniqueList.append(i)

        # Setting the new search tuple to continue iterating
        if len(nextTarget) == 1:
            searching = uniqueList[0]
        else:
            searching = random.choice(uniqueList)


    return observedCount, totalDistance
