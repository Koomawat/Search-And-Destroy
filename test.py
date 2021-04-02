import numpy as np
import random

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

    testBoard[0,0] = testBoard[0,0] * 0.3

    print(testBoard)

    sumA = np.sum(testBoard)
    print(sumA)

    testBoard2 = testBoard / sumA

    print(testBoard2)

    return


if __name__ == "__main__":
    main()