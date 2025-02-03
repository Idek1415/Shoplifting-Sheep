
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
        if (G.testPlace(choice[0], choice[1]) == True):
            N.fitness += 1
    

def trainGeneration(population, Games):

    for N in population:
        determineFitness(N, Games)
    
    population.sort(key=lambda N: N.fitness, reverse=True)

    newPopulation = []
    for i in range(5):
        for nN in range(4 * (5-i)):
            newLarry = deepcopy(population[i])
            if (nN != 0):
                newLarry.mutate()
            newPopulation.append(newLarry)
     
    return newPopulation


def trainAlgorithm(numGenerations = 0):
    Games = getBoards(startTurn = 0, endTurn= 4)

    print(len(Games))
    
    
    population = [Network(layer_nums = [16,13,16]) for n in range(60)]

    for g in range(numGenerations):
        population = trainGeneration(population, Games)
        print(population[0].fitness)



trainAlgorithm(numGenerations = 1000)