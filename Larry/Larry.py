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
        
        self.memory = []
    
    def addMemory(self, board, choice, value):
        self.memory.append((board, choice, value))
        
    def sigmoid(self, value):
        return 1.0/ (1.0 + np.exp(-value))
    
    def getPlacement(self, Game):
        inputs = Game.getInputs(1)

        self.propogate(inputs = inputs)

        legalChoice = False

        while (legalChoice == False):
            index = list(self.outputs).index(max(self.outputs))
            choice = [(index % 4), (int)(index / 4)]
            legalChoice = Game.testPlace(choice[0],choice[1])
            if (legalChoice == False):
                self.outputs[index] = 0.0
        
        return choice    
    
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
        self.network = Network(layer_nums=[17,15,17])
    

    def getChoice(self, Game):
        inputs = Game.getInputs() + [0.0]

        self.network.propogate(inputs= inputs)
        choice = self.getLegalChoice(Game)

        if (self.network.outputs[16] > 0.5):
            inputs[16] = 1.0
            self.network.propogate(inputs = inputs)
            choice += self.getLegalChoice(Game)
        

    def getLegalChoice(self, Game):
        legalChoice = False

        while (legalChoice == False):
            index = list(self.outputs).index(max(self.outputs))
            choice = [(index % 4), (int)(index / 4)]
            legalChoice = Game.testPlace(choice[0],choice[1])
            if (legalChoice == False):
                self.outputs[index] = 0.0
        
        return choice    

        