import numpy as np
import random

def main():

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
    
    #print()

    searching3 = random.choice(visiting)

    print()
    print("Observing: ", searching3)

    if searching == searching3:
        print("Target found.")
    else:

        supposeTrue = testBoard[searching3] * 0.3
        testBoard[searching3] = (supposeTrue) / ((1 - testBoard[searching3]) + supposeTrue)
        
        #print()
        #print(testBoard)

        visiting.remove(searching3)
        #print(observedList)
        for i in range(len(observedList)):
            #supposeTrue = testBoard[observedList[i]] * 0.3
            testBoard[observedList[i]] = supposeTrue / ((1 - testBoard[observedList[i]]) + supposeTrue)

        observedList.append(searching3)

        observedCount += 1

        #print(visiting)

        for i in range (3):
            for j in range(3):
                if (i,j) in visiting:
                    testBoard[(i,j)] = testBoard[(i,j)] / ((1 - testBoard[(i,j)] + supposeTrue))

        print()
        print(testBoard)

    return


if __name__ == "__main__":
    main()