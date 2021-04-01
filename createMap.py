import numpy as np
import random

def board(dim):

    gameboard = np.zeros(shape=(dim,dim), dtype=object)

    return gameboard


def makeTerrain(terrainMap):

    # Possible Terrain Choices

    terrainChoices = ["Flat", "Hilly", "Forested", "Caves"]

    # Randomly setting a cell to a terrain type with each terrain having 1/4 chance

    for i in range(50):
        for j in range(50):

            terrianType = random.choice(terrainChoices)

            # 'f' designates Flat

            if(terrianType == "Flat"):
                terrainMap[i,j] = 'f'

            # 'H' designates Hilly

            elif (terrianType == "Hilly"):
                terrainMap[i,j] = 'H'

            # 'F' designates Forest

            elif (terrianType == "Forest"):
                terrainMap[i,j] = 'F'

            # 'C' designates Caves

            else:
                terrainMap[i,j] = 'C'


    return terrainMap


def shortestDistance(matrix):


    return