from Boards import Game
import Larry
import os
import pickle

def getBestLarry():
    BestLarry = None

    try: 
        LarryFile = open('Larry_Storage.txt', 'rb')
        population = pickle.load(LarryFile)
        LarryFile.close()
        BestLarry = population[0]
    except FileNotFoundError: 
        print("Larry declines your offer to play.")
    
    return BestLarry

def playGame():
    game = Game()

    larry = getBestLarry()
    if (larry == None): return 

    for turn in range(16):
        os.system('clear')
        #print(game.has_won())
        choice = larry.getPlacement(game)
        game.board[choice[1]][choice[0]] = 1
        
        game.display()

        if (game.has_won() != 0):
            print("Larry has won")
            return

        col = int(input("Enter Column(1-4): ")) - 1
        row = int(input("Enter Row(1-4): ")) - 1

        game.board[row][col] = -1

        if (game.has_won() != 0):
            print("You have won")
            return
        

playGame()