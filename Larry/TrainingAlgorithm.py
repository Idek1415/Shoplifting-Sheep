import time 
from copy import deepcopy
import numpy as np
from Larry import Network
from Boards import Game
from Boards import getBoards

def determineFitness(N, Games):
    N.fitness = 0
    for G in Games:
        choice = N.getPlacement(G)
        if (G.testPlace(choice[1][0]) == True):
            N.fitness += 1
    

def trainGeneration(population, Games):

    for N in population:
        determineFitness(N, Games)
    
    population.sort(reverse = True, key = N.fitness)

    newPopulation = []
    for i in range(5):
        for nN in range(4 * (5-i)):
            newLarry = deepcopy(population[i])
            if (nN != 0):
                newLarry.mutate()
            newPopulation.append(newLarry)
     
    return newPopulation


def trainAlgorithm(numGenerations = 0):
    Games = getBoards(endTurn= 8)

    population = [Network() for n in range(60)]

    for g in range(numGenerations):
        population = trainGeneration(population, Games)


trainAlgorithm()