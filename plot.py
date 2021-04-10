from basicAgent1 import *
from basicAgent2 import *
from mapFunctions import *
from improvedAgent import *
from printMap import *
import sys
from matplotlib import pyplot as plt

# Plot both types of data analysis on subplots
def both():

    # Get the dimension of the map
    dim = int(input("Enter the dimension of the map: "))

    # Empty lists for later to append on averages for each map traversed by different agents
    mapType_list = []
    avg_list = []
    agent1_avg_list, agent2_avg_list, improved_avg_list = [], [], []

    # 10 different maps
    for i in range(11):

        # Set random board each time
        np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)
        mapGrid = board(dim)
        mapGrid, _ = makeTerrain(mapGrid)

        # Lists to add on scores
        total_list = []
        agent1_total_list, agent2_total_list, improved_total_list = [], [], []

        # 10 different runthrough with different target and initial location each time
        for j in range(11):
            
            # Random target location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            targetLocation = (randX, randY)

            # Random initial location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            initialLocation = (randX, randY)

            # Same belief state for all agents
            beliefState = agentBoard(dim)
            # Get how many searches and distances 
            agent1searches, agent1distance = calculateContainingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            agent2searches, agent2distance = calculateFindingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            improvedSearches, improvedDistance = calculateImprovedBelief(mapGrid, beliefState, targetLocation, initialLocation)

            # Get score
            agent1total = agent1searches + agent1distance
            agent2total = agent2searches + agent2distance
            improvedTotal = improvedSearches + improvedDistance

            # For Plot 2
            agent1_total_list.append(agent1total)
            agent2_total_list.append(agent2total)
            improved_total_list.append(improvedTotal)

            # For Plot 1
            totalPerRun = [agent1total, agent2total, improvedTotal]
            total_list.append(totalPerRun)
            print(j)
        print(i)

        # For Plot 2
        agent1avg = sum(agent1_total_list) / 10
        agent2avg = sum(agent2_total_list) / 10
        improvedAvg = sum(improved_total_list) / 10
        agent1_avg_list.append(agent1avg)
        agent2_avg_list.append(agent2avg)
        improved_avg_list.append(improvedAvg)

        # For Plot 1
        avgPerMap_sum = [sum(k) for k in zip(*total_list)]
        avgPerMap = [k / 10 for k in avgPerMap_sum]
        avg_list.append(avgPerMap)

    # Subplots for different graphs
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Performance of Agents')

    ###############################################################
    ####### Plot 1 ################################################
    ###############################################################

    xax = ["Agent 1", "Agent 2", "Improved Agent"]
    overallAvg_sum = [sum(k) for k in zip(*avg_list)]
    overallAvg = [k / 10 for k in overallAvg_sum]
    ax1.plot(xax, overallAvg, label = "Total")

    # Axis labeling and other plot display features
    ax1.set_xlabel('Agent Type')
    ax1.set_ylabel('Score')
    ax1.set_title(f"Overall Performance Per Agent\nMap dimension: {dim} x {dim}")
    ax1.legend(loc = "upper right")

    ###############################################################
    ####### Plot 2 ################################################
    ###############################################################

    xax = ["M"+str(k) for k in range(11)]
    ax2.plot(xax, agent1_avg_list, label = "Agent 1")
    ax2.plot(xax, agent2_avg_list, label = "Agent 2")
    ax2.plot(xax, improved_avg_list, label = "Improved Agent")
    # Axis labeling and other plot display features
    ax2.set_xlabel('Map List')
    ax2.set_ylabel('Score')
    ax2.set_title(f"Performance of Agents Per Map\nMap dimension: {dim} x {dim}")
    ax2.legend(loc = "upper right")


    plt.show()

# Plotting based on 10 different maps over 10 different runthroughs for each agent
def plot2(): 

    # Get the dimension of the map
    dim = int(input("Enter the dimension of the map: "))

    # Empty lists for later to append on averages for each map traversed by different agents
    agent1_avg_list, agent2_avg_list, improved_avg_list = [], [], []

    # 10 different maps
    for i in range(11):

        # Set random board each time
        np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)
        mapGrid = board(dim)
        mapGrid, _ = makeTerrain(mapGrid)

        # Lists to add on score for each agent type
        agent1_total_list, agent2_total_list, improved_total_list = [], [], []

        # 10 different runthrough with different target and initial location each time
        for j in range(11):

            # Random target location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            targetLocation = (randX, randY)

            # Random initial location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            initialLocation = (randX, randY)

            # Same belief state for all agents
            beliefState = agentBoard(dim)
            # Get how many searches and distances 
            agent1searches, agent1distance = calculateContainingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            agent2searches, agent2distance = calculateFindingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            improvedSearches, improvedDistance = calculateImprovedBelief(mapGrid, beliefState, targetLocation, initialLocation)
            
            # Get score and add to score list
            agent1total = agent1searches + agent1distance
            agent1_total_list.append(agent1total)
            agent2total = agent2searches + agent2distance
            agent2_total_list.append(agent2total)
            improvedTotal = improvedSearches + improvedDistance
            improved_total_list.append(improvedTotal)
            print(j)

        # For each agent, take an average per map
        agent1avg = sum(agent1_total_list) / 10
        agent2avg = sum(agent2_total_list) / 10
        improvedAvg = sum(improved_total_list) / 10
        agent1_avg_list.append(agent1avg)
        agent2_avg_list.append(agent2avg)
        improved_avg_list.append(improvedAvg)
        print(i)

    # x-axis labels
    xax = ["M"+str(k) for k in range(11)]

    # Different lines per agent
    plt.plot(xax, agent1_avg_list, label = "Agent 1")
    plt.plot(xax, agent2_avg_list, label = "Agent 2")
    plt.plot(xax, improved_avg_list, label = "Improved Agent")

    # Axis labeling and other plot display features
    plt.xlabel('Map List')
    plt.ylabel('Score')
    plt.title(f"Performance of Agents Per Map\nMap dimension: {dim} x {dim}")
    plt.legend(loc = "upper right")
    plt.show()

# Plotting based on agent type over 10 different runthroughs for 10 maps
def plot1(): 

    # Get the dimension of the map
    dim = int(input("Enter the dimension of the map: "))

    # Empty lists for later to append on averages for each map traversed by different agents
    avg_list = []

    # 10 different maps
    for i in range(11):

        # Set random board each time
        np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)
        mapGrid = board(dim)
        mapGrid, _ = makeTerrain(mapGrid)

        # Lists to add on scores
        total_list = []

        # 10 different runthrough with different target and initial location each time
        for j in range(11):

            # Random target location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            targetLocation = (randX, randY)

            # Random initial location
            randX = random.randint(0,dim-1)
            randY = random.randint(0,dim-1)
            initialLocation = (randX, randY)

            # Same belief state for all agents
            beliefState = agentBoard(dim)
            # Get how many searches and distances 
            agent1searches, agent1distance = calculateContainingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            agent2searches, agent2distance = calculateFindingBelief(mapGrid, beliefState, targetLocation, initialLocation)
            improvedSearches, improvedDistance = calculateImprovedBelief(mapGrid, beliefState, targetLocation, initialLocation)
            
            # Get score
            agent1total = agent1searches + agent1distance
            agent2total = agent2searches + agent2distance
            improvedTotal = improvedSearches + improvedDistance

            # Add as a set
            totalPerRun = [agent1total, agent2total, improvedTotal]
            total_list.append(totalPerRun)
            print(totalPerRun)

        # For each agent, take an average 
        # (divided by 10 since 10 different runthroughs)
        avgPerMap_sum = [sum(k) for k in zip(*total_list)]
        avgPerMap = [k / 10 for k in avgPerMap_sum]
        avg_list.append(avgPerMap)

    # Take average again 
    # (divided by 10 since 10 different maps)
    overallAvg_sum = [sum(k) for k in zip(*avg_list)]
    overallAvg = [k / 10 for k in overallAvg_sum]

    # x-axis labels
    xax = ["Agent 1", "Agent 2", "Improved Agent"]
    plt.plot(xax, overallAvg, label = "Total")
    # Axis labeling and other plot display features
    plt.xlabel('Agent Type')
    plt.ylabel('Score')
    plt.title(f"Performance Based On Agent Type\nMap dimension: {dim} x {dim}")
    plt.legend(loc = "upper right")
    plt.show()

def main():

    # plot1()
    # plot2()
    both()

    return

if __name__ == "__main__":
    main()