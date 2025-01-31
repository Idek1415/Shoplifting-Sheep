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
        testSums = []
        for r in range(4):
            for c in range(4):
                val = self.board[r][c]
                if (val != 0):
                    testSums[0] += val
                else:
                    testSums[0] = 0
        for r in range(4):
            for c in range(4):
                val = self.board[c][r]
                if (val != 0):
                    testSums[1] += val
                else:
                    testSums[1] = 0
        
        for i in range(3):
            testSums[2] += self.board[1+i][i]
            if (self.board[1+i][i] == 0):
                testSums[0] = 0
            testSums[3] += self.board[i][1+i]
            if (self.board[i][1+i] == 0):
                testSums[1] = 0
            testSums[4] += self.board[2-i][i]
            if (self.board[2-i][i] == 0):
                testSums[2] = 0
            testSums[5] += self.board[3-i][1+i]
            if (self.board[3-i][1+i] == 0):
                testSums[3] = 0
        for i in range(4):
            testSums[6] += self.board[i][i]
            if (self.board[i][i] == 0):
                    testSums[4] = 0
            testSums[7] += self.board[3-i][i]
            if (self.board[3-i][i] == 0):
                    testSums[5] = 0

        for sum in testSums:
            if (sum >= 3):
                return 1
            if (sum <= -3):
                return -1
        
        return 0


def getBoards(startTurn = 0, endTurn = 0, currentTurn = 0, lastSeed = [0 for i in range(16)], boards = []):
    
    if (currentTurn == endTurn):
        return boards

    for i in range(16):
        seed = lastSeed
        if (seed[i] == 0):
            if (currentTurn % 2 == 0):
                seed[i] = -1
            else:
                seed[i] = 1
            newGame = Game(inputs = seed)
            if (currentTurn >= startTurn):
                boards.append(newGame)
            getBoards(currentTurn = currentTurn + 1, lastSeed = seed, boards = boards)
