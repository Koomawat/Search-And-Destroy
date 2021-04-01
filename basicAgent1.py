
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
    unvisited = []

    # Observed list to keep track of which cells of the map have been searched
    observed = []

    # Counter to keep track of total distance agent travels
    totalDistance = 0

    # Counter to keep track of number of searched conducted by the agent
    observedCount = 0

    # Target found boolean so we keep iterating until the target is found
    targetFound = False


    agentsBoard = matrix


    boardDim = len(beliefState)


    for i in range(boardDim):
        for j in range(boardDim):
            agentsBoard[i,j] = 1 / boardDim
            unvisited.append((i,j))


    #while targetFound == False:

        # (P(Cell x = T) P(Cell y = F | Cell x = T))

        #beliefXY = 0


        #return

    return agentsBoard


