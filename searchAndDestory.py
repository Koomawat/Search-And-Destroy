from basicAgent1 import *
from basicAgent2 import *
from createMap import *
from improvedAgent import *
from printMap import *
import sys

def main():

    np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)

    mapGrid = board(10)

    mapGrid, targetLocation = makeTerrain(mapGrid)
    print()
    print("Target at location: ", targetLocation)
    print("Terrain type: ", mapGrid[targetLocation])

    print()
    printBoard(mapGrid)

    agent1BeliefState = board(10)
    agent2BeliefState = board(50)
    improvedAgentBeliefState = board(50)

    answer = calculateBelief(mapGrid, agent1BeliefState, targetLocation)

    print(answer)

    return


if __name__ == "__main__":
    main()