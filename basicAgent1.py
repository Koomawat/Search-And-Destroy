import random

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
            agentsBoard[i,j] = 1 / boardDim
            tuples.append((i,j))

    # Initial cell agent will search
    searching = random.choice(tuples)
    
    #while targetFound == False:
    if 1 == 1:


        currentTerrain = agentsBoard[searching]


        falseNegative = 0


        if currentTerrain == 'f':
            falseNegative = 0.1
        elif currentTerrain == 'H':
            falseNegative = 0.3
        elif currentTerrain == 'F':
            falseNegative = 0.7
        else:
            falseNegative = 0.9


        if searching == targetLocation:

            num = falseNegativeCheck()

            if num > falseNegative:
                print("Target Found!")
                return agentsBoard
        

        #(P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefNumerator = belief[searching] * falseNegative

        #(P(Cell x = F) + P(Cell x = T) P(Cell y = F | Cell x = T))
        observingBeliefDenominator = (1 - belief[searching]) + observingBeliefNumerator
    


    maxList = largestProbabilities(belief)
    

        #return

    return agentsBoard


def falseNegativeCheck():

    number = random.uniform(0,1)

    return number


def largestProbabilities(belief):

    maxList = []

    maxVal = belief[0,0]
    maxList.append((0,0))

    for i in range(len(belief)):
        for j in range(len(belief)):
            if belief[i,j] == maxVal:
                maxList.append((i,j))
            if belief[i,j] > maxVal:
                maxList = []
                maxList.append((i,j))

    return maxList
