import numpy as np
import random

def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard


def makeTerrain(terrainMap):

    # Possible Terrain Choices

    terrainChoices = ["Flat", "Hilly", "Forested", "Caves"]

    # Randomly setting a cell to a terrain type with each terrain having 1/4 chance

    for i in range(len(terrainMap)):
        for j in range(len(terrainMap)):

            terrianType = random.choice(terrainChoices)

            # 'f' designates Flat

            if(terrianType == "Flat"):
                terrainMap[i,j] = 'f'

            # 'H' designates Hilly

            elif (terrianType == "Hilly"):
                terrainMap[i,j] = 'H'

            # 'F' designates Forest

            elif (terrianType == "Forested"):
                terrainMap[i,j] = 'F'

            # 'C' designates Caves

            else:
                terrainMap[i,j] = 'C'

    lenTerrain = len(terrainMap)
    randX = random.randint(0,lenTerrain-1)
    randY = random.randint(0,lenTerrain-1)
    targetLocation = (randX, randY)

    return terrainMap, targetLocation


def shortestDistance(matrix, start, goal):

    return