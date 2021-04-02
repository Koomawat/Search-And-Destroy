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
            testBoard[i,j] = 1/2
            visiting.append((i,j))

    testBoard = testBoard * 10000

    print(testBoard)

    return


if __name__ == "__main__":
    main()