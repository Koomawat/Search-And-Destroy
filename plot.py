from basicAgent1 import *
from basicAgent2 import *
from mapFunctions import *
from improvedAgent import *
from printMap import *
import sys
from matplotlib import pyplot as plt

def plot(): 

    dim = int(input("Enter the dimension of the map: "))

    avg_list = []

    for i in range(1):
        np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)
        mapGrid = board(dim)
        mapGrid, _ = makeTerrain(mapGrid)

        total_list = []

        for j in range(1):
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            targetLocation = (randX, randY)

            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            initialLocation = (randX, randY)

            beliefState = agentBoard(dim)
            print('asdf1')
            agent1searches, agent1distance = calculateContainingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            print('asdf2')
            agent2searches, agent2distance = calculateFindingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            print('asdf3')
            improvedSearches, improvedDistance = calculateImprovedBelief(mapGrid, beliefState, targetLocation, initialLocation)
            print('asdf4')

            agent1total = agent1searches + agent1distance
            agent2total = agent2searches + agent2distance
            improvedTotal = improvedSearches + improvedDistance

            totalPerRun = [agent1total, agent2total, improvedTotal]
            total_list.append(totalPerRun)
            print('asdf')

        print(total_list)
        avgPerMap_sum = [sum(k) for k in zip(*total_list)]
        avgPerMap = [k / 10 for k in avgPerMap_sum]
        avg_list.append(avgPerMap)

    xax = ["Agent 1", "Agent 2", "Improved Agent"]

    overallAvg_sum = [sum(k) for k in zip(*avg_list)]
    overallAvg = [k / 10 for k in overallAvg_sum]
    
    plt.plot(xax, overallAvg, label = "Total")

    # Axis labeling and other plot display features
    plt.xlabel('Agent Type')
    plt.ylabel('Score')
    plt.title(f"Performance Based On Agent Type\nMap dimension: {dim} x {dim}")
    plt.legend(loc = "upper right")
    plt.show()

def main():

    plot()

    return


if __name__ == "__main__":
    main()