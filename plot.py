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

    for i in range(11):
        np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)
        mapGrid = board(dim)
        mapGrid, _ = makeTerrain(mapGrid)

        total_list = []

        for j in range(11):
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            targetLocation = (randX, randY)

            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            initialLocation = (randX, randY)

            beliefState = agentBoard(dim)
            agent1searches, agent1distance = calculateContainingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            agent2searches, agent2distance = calculateFindingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            improvedSearches, improvedDistance = calculateImprovedBelief(mapGrid, beliefState, targetLocation, initialLocation)
            
            agent1total = agent1searches + agent1distance
            agent2total = agent2searches + agent2distance
            improvedTotal = improvedSearches + improvedDistance

            totalPerRun = [agent1total, agent2total, improvedTotal]
            print(totalPerRun)
            total_list.append(totalPerRun)

        avgPerMap_sum = [sum(k) for k in zip(*total_list)]
        avgPerMap = [k / 10 for k in avgPerMap_sum]
        avg_list.append(avgPerMap)

    xax = ["Agent 1", "Agent 2", "Improved Agent"]

    print(avg_list)
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