import time 
import os
from copy import deepcopy
import numpy as np
from Larry import Network
from Boards import Game
from Boards import getBoards
import pickle

def determineFitness(N, Games):
    tic = time.process_time()
    N.fitness = 0
    for G in Games:
        choice = N.getPlacement(G)
        if (G.testPlace(choice[0], choice[1]) == True):
            N.fitness += 1
            G.board[choice[1]][choice[0]] = 1
            if (G.has_won() == 1):
                N.fitness += 10
            G.board[choice[1]][choice[0]] = 0
        
    toc = time.process_time()
    print("Computation time = " + str(1000*(toc - tic )) + "ms              " + str(int(N.fitness * 100/len(Games))) + "%")
    learningRateData = open("data.txt",'a')
    learningRateData.write((str(N.fitness)) + "\n")
    learningRateData.close()
    

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


def trainAlgorithm(numGenerations = 0, reset = False):
   
    Games = getBoards(startTurn = 0, endTurn= 4)
    print(len(Games))


    if(reset == True):
        os.remove("data.txt")
        population = [Network(layer_nums = [16,13,16]) for n in range(60)]
    else:
        try:
            LarryFile = open('Larry_Storage.txt', 'rb')
            population = pickle.load(LarryFile)
            LarryFile.close()
        except FileNotFoundError:
            population = [Network(layer_nums = [16,13,16]) for n in range(60)]
    


    for g in range(numGenerations):
        print("\n\nGeneration: " + str(g) + ": " + str(population[0].fitness) + "\n")

        population = trainGeneration(population, Games)
        LarryFile = open('Larry_Storage.txt', 'wb')
        pickle.dump(population, LarryFile)             
        LarryFile.close()




trainAlgorithm(numGenerations = 1000)