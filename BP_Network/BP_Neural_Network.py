import numpy as np
import time 
import random

class Network():
    
    def __init__ (self, layer_nums = [], learning_rate = 1.0):
        self.layers = len(layer_nums)
        self.hidden_layers = self.layers - 2

        self.learning_rate = learning_rate
        self.outputs = [0.0 for o in range(layer_nums[self.layers-1])]
        self.hidden_outputs = [[] for layer in range(self.hidden_layers + 1)] 

        self.biases = ([[random.uniform(-1.0,1.0) for node in range(layer_nums[layer + 1])] for layer in range(self.hidden_layers + 1)])
        self.weights = ([[[random.uniform(-1.0,1.0) for nextNode in range(layer_nums[layer + 1])] for node in range(layer_nums[layer])] for layer in range(self.hidden_layers + 1)])
        
    def sigmoid(self, value):
        return 1.0/ (1.0 + np.exp(-value))
    
    def sigmoid_prime(self, value):
        return self.sigmoid(value) * (1-self.sigmoid(value))

    def get_layer_outputs(self, inputs, layer):
        return self.sigmoid(np.dot(inputs, self.weights[layer]) + self.biases[layer])


    def propogate(self, inputs = [], current_layer = 0):
        self.hidden_outputs[current_layer] = self.get_layer_outputs(inputs, current_layer)       #adds hidden outputs

        if current_layer == self.hidden_layers:
            self.outputs = self.hidden_outputs[current_layer]
        else:
            self.propogate(self.hidden_outputs[current_layer], current_layer= current_layer + 1)
    
    def backpropogate(self, error, current_layer, delta = None):
        if (current_layer < 0):         #End Recursion
            return
        
        
        if (current_layer != self.hidden_layers):       #    For Hidden Layers
            error = np.dot(delta, np.array(self.weights[current_layer+1]).T)
            delta = error * self.sigmoid_prime(self.hidden_outputs[current_layer])

            
            #print("TEST " + str(current_layer) + str(error))
        
        else:           #   For Output Layer
            delta = error * self.sigmoid_prime(self.hidden_outputs[current_layer])
            #print("TEST " + str(current_layer) + str(error))
            


        self.biases[current_layer] += np.sum(delta, axis=0, keepdims=True) * self.learning_rate
        self.weights[current_layer] += np.dot(np.array(self.hidden_outputs[current_layer]).T, delta) * self.learning_rate

        self.backpropogate(error, current_layer-1, delta= delta)

    def mutate_weights(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):
        for l in self.weights:
            for n in l:
                for w in n:
                    w += random.uniform(-1.0,1.0) * MUTATE_MAGNITUDE

    def mutate_biases(self, MUTATE_MAGNITUDE = 1.0, MUTATE_PERCENTAGE = 1.0):

        for l in self.biases:
            for b in l:
                b += random.uniform(-1.0, 1.0) * MUTATE_MAGNITUDE
        
    
















