from basicAgent1 import *
from basicAgent2 import *
from createMap import *
from improvedAgent import *
from printMap import *

def main():

    mapGrid = board(50)

    mapGrid = makeTerrain(mapGrid)

    printBoard(mapGrid)

    agent1BeliefState = board(50)
    agent2BeliefState = board(50)
    improvedAgentBeliefState = board(50)

    return


if __name__ == "__main__":
    main()