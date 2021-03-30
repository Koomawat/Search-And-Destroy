import numpy as np
import random

from numpy.core.defchararray import add

def main():

    np.set_printoptions(precision=4)

    testBoard = np.zeros((3,3))

    visiting = []

    print(testBoard)

    for i in range(3):
        for j in range(3):
            testBoard[i,j] = 1/9
            visiting.append((i,j))

    #print(visiting)
    print()
    print(testBoard)
    print()

    searching = random.choice(visiting)

    print("Target at: ", searching)

    searching2 = random.choice(visiting)

    print("Observing: ", searching2)

    observedCount = 0

    observedList = []

    if searching == searching2:
        print("Target found.")
    else:

        supposeTrue = testBoard[searching2] * 0.3
        testBoard[searching2] = (supposeTrue) / ((1 - testBoard[searching2]) + supposeTrue)
        
        visiting.remove(searching2)
        observedList.append(searching2)

        observedCount += 1

        for i in range (3):
            for j in range(3):
                if (i,j) in visiting:
                    testBoard[(i,j)] = testBoard[(i,j)] / ((1 - testBoard[(i,j)] + supposeTrue))

        print()
        print(testBoard)
        adding = np.sum(testBoard)
        print()
        print("Adds to: ", adding)
    
    #print()

    searching3 = random.choice(visiting)

    print()
    print("Observing: ", searching3)

    if searching == searching3:
        print("Target found.")
    else:

        supposeTrue = testBoard[searching3] * 0.3
        supposeTruer = ((1 - testBoard[searching3]) + supposeTrue)
        
        testBoard[searching3] = (supposeTrue) / ((1 - testBoard[searching3]) + supposeTrue)
        
        #print()
        #print(testBoard)

        visiting.remove(searching3)
        #print()
        #print(testBoard)
        ##print(observedList)
        for i in range(len(observedList)):
            #supposeTrue = testBoard[observedList[i]] * 0.3
            testBoard[observedList[i]] = testBoard[observedList[i]] / supposeTruer

        observedList.append(searching3)

        observedCount += 1

        #print(visiting)

        visitingLen = len(visiting)

        for i in range (3):
            for j in range(3):
                if (i,j) in visiting:
                    testBoard[(i,j)] = testBoard[(i,j)] / ((1 - testBoard[(i,j)] + supposeTrue))

        print()
        print(testBoard)
        adding = np.sum(testBoard)
        print()
        #print(adding)
        print("Adds to: ", adding)
    return


if __name__ == "__main__":
    main()