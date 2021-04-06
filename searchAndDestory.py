from basicAgent1 import *
from basicAgent2 import *
from mapFunctions import *
from improvedAgent import *
from printMap import *
import sys

def main():

    np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)

    mapGrid = board(50)

    mapGrid, targetLocation = makeTerrain(mapGrid)
    print()
    print("Target at location: ", targetLocation)
    print("Terrain type: ", mapGrid[targetLocation])
    print()
    #printBoard(mapGrid)

    agent1BeliefState = agentBoard(50)
    agent2BeliefState = agentBoard(50)
    improvedAgentBeliefState = board(50)

    # Basic Agent 1/2 searches
    agent1searches, agent1distance = calculateContainingBelief(mapGrid, agent1BeliefState, targetLocation)
    agent2searches, agent2distance = calculateFindingBelief(mapGrid, agent2BeliefState, targetLocation)

    print("Agent 1 Distance: ", agent1distance)
    print("Agent 1 Searches: ", agent1searches)

    agent1total = agent1searches + agent1distance
    print("Agent 1 Total =", agent1total)

    print()

    print("Agent 2 Distance: ", agent2distance)
    print("Agent 2 Searches: ", agent2searches)

    agent2total = agent2searches + agent2distance
    print("Agent 2 Total =", agent2total)


    return


if __name__ == "__main__":
    main()