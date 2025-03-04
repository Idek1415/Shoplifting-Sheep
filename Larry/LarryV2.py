import numpy as np
import random
from copy import deepcopy


class Network():
    
    def __init__ (self, layer_nums = [], seed = None):

        if (seed != None):
            self.layers = seed.layers
            self.hidden_layers = self.layers - 2
            self.outputs = [0.0 for o in range(layer_nums[self.layers-1])]
            self.biases = seed.biases
            self.weights = seed.weights
            self.fitness = seed.fitness
        
        else:
            self.layers = len(layer_nums)
            self.hidden_layers = self.layers - 2

            self.outputs = [0.0 for o in range(layer_nums[self.layers-1])]

            self.biases = ([[random.uniform(-1.0,1.0) for node in range(layer_nums[layer + 1])] for layer in range(self.hidden_layers + 1)])
            self.weights = ([[[random.uniform(-1.0,1.0) for nextNode in range(layer_nums[layer + 1])] for node in range(layer_nums[layer])] for layer in range(self.hidden_layers + 1)])

            self.fitness = 0
        
    def sigmoid(self, value):
        return 1.0/ (1.0 + np.exp(-value))    
    
    def propogate(self, inputs = [], current_layer = 0):
        hidden_output = self.sigmoid(np.dot(inputs, self.weights[current_layer]) + self.biases[current_layer])

        if current_layer == self.hidden_layers:
            self.outputs = hidden_output
            return self.outputs
        else:
            self.propogate(hidden_output, current_layer= current_layer + 1)

    def mutate(self):
        self.mutate_weights(MUTATE_MAGNITUDE= 0.1, MUTATE_PERCENTAGE= 0.1)
        self.mutate_biases(MUTATE_MAGNITUDE= 0.1, MUTATE_PERCENTAGE= 0.1)

    def mutate_weights(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):
        for l in range(len(self.weights)):
            for n in range(len(self.weights[l])):
                for w in range(len(self.weights[l][n])):
                    if (random.random() < MUTATE_PERCENTAGE):
                        self.weights[l][n][w] += random.uniform(-1.0,1.0) * MUTATE_MAGNITUDE

    def mutate_biases(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):
        for l in range(len(self.biases)):
            for b in range(len(self.biases[l])):
                if (random.random() < MUTATE_PERCENTAGE):
                    self.biases[l][b] += random.uniform(-1.0, 1.0) * MUTATE_MAGNITUDE




class Larry():

    def __init__(self):
        self.playerVal = 1
        self.placeNetwork = Network(layer_nums=[32, 16, 16])
    
    def addMemory(self):
        pass

    def getPlaceChoice(self, game):
        choice = []
        inputs = game.getInputs(self.playerVal) + self.placeNetwork.outputs

        outputs = list(self.placeNetwork.propogate(inputs))

        for o in range(len(outputs)):
            if game.testPlace(o%4 , int(o/4)) == False:
                outputs[o] = 0.0
            
            elif game.testWin(o%4 , int(o/4)) == True:
                outputs[0] = 1.0
        
        index = outputs.index(max(outputs))
        choice = [index%4, int(index/4)]
        return choice
    











    def addMemory(self, board, choice, value):
        self.memory.append((board, choice, value))