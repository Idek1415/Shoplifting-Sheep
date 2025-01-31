import numpy as np
import random


class Network():
    
    def __init__ (self, layer_nums = [], seed = None, learning_rate = 1.0):

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
    
    def getPlacement(self, Game):
        inputs = Game.inputs(1)

        self.propogate(inputs = inputs)

        legalChoice = False

        while (legalChoice == False):
            index = self.outputs.index(max(self.outputs))
            choice = [index / 4][index % 4]
            legalChoice == True
        

    def propogate(self, inputs = [], current_layer = 0):
        hidden_output = self.sigmoid(np.dot(inputs, self.weights[current_layer]) + self.biases[current_layer])

        if current_layer == self.hidden_layers:
            self.outputs = hidden_output
        else:
            self.propogate(self.hidden_output, current_layer= current_layer + 1)

    def mutate(self):
        self.mutate_weights(MUTATE_MAGNITUDE= 0.5, MUTATE_PERCENTAGE=0.25)
        self.mutate_biases(MUTATE_MAGNITUDE= 0.2, MUTATE_PERCENTAGE= 0.25)

    def mutate_weights(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):
        for l in self.weights:
            for n in l:
                for w in n:
                    w += random.uniform(-1.0,1.0) * MUTATE_MAGNITUDE

    def mutate_biases(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):
        for l in self.biases:
            for b in l:
                b += random.uniform(-1.0, 1.0) * MUTATE_MAGNITUDE