import numpy as np
from copy import deepcopy

class Game():
    
    def __init__(self, inputs = [0 for i in range(16)]):
        self.board = []
        for r in range(4):
            row = []
            for c in range(4):
                row.append(inputs[(4*r)+c])
            self.board.append(row)
    
    def display(self):
        for row in self.board:
            string = ""
            for col in row:
                if(col == -1):
                    string += "| O |"
                elif (col == 1):
                    string += "| X |"
                else:
                    string += "|   |"
            print(string)
            print("--------------------")

    def getInputs(self, player):
        inputs = []
        for row in self.board:
            inputs += row
        return (player * inputs)
    
    def testPlace(self, x, y):
        if (self.board[y][x] == 0):
            return True
        return False
    
    def testBump(self, x, y, xB, yB):
        if (self.board[y][x] == -1 and self.testPlace(xB, yB) == True):
            return True
        return False

    def has_won(self):
        for row in self.board:
            testSum = 0
            for col,val in enumerate(row):
                if (val == 0 and col != 0 and col != 3): testSum = 0
                testSum += val
            if (testSum >= 3): return 1
            if (testSum <= -3): return -1

        for col in range(4):
            testSum = 0
            for row in range(4):
                val = self.board[row][col]
                if (val == 0 and row != 0 and row != 3): testSum = 0
                testSum += val
            if (testSum >= 3): return 1
            if (testSum <= -3): return -1

        diagonals = [0,0,0,0,0,0]

        for i in range(3):
            diagonals[0] += self.board[1+i][i]
            diagonals[1] += self.board[i][1+i]
            diagonals[2] += self.board[2-i][i]
            diagonals[3] += self.board[3-i][1+i]

        for i in range(4):
            diagonals[4] += self.board[i][i]
            if (self.board[i][i] == 0 and i != 0 and i != 3): diagonals[4] = 0
            diagonals[5] += self.board[3-i][i]
            if (self.board[3-i][i] == 0 and i != 0 and i != 3): diagonals[5] = 0
        
        for val in diagonals: 
            if (val >= 3): return 1
            if (val <= -3): return -1
        
        return 0

            
            
def getBoards(startTurn = 0, endTurn = 0):
    boards = []
    indices = [-1 for t in range(endTurn)]
    
    index = 0
    adding = False
    
    while index < endTurn:
        
        indices[index] += 1
        
        if (indices.index(indices[index]) != index):
            indices[index] += 1
        
        if (indices[index] >= 16):
            indices[index] = 0
            adding = True
            index += 1 
        
        else:
            adding = False
            seed = [0 for t in range(16)]
            
            for i,val in enumerate(indices):
                if (val > 0):
                    if ((i+1) % 2 == 0):
                        seed[val] = -1
                    else:
                        seed[val] = 1
            G = Game(inputs = seed)
            
            if (G.has_won() == 0 and indices[startTurn] != -1):
                boards.append(G)
            
            index = 0

    return boards  
    
    
    
            