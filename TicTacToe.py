import random
import Board

class TicTacToe:

    def __init__(self):
        self.boardSize = self.gameSetup()
        self.numPlayers = self.gameMode()
        self.difficulty = 0 if self.numPlayers == 2 else self.gameDifficulty()
        self.board = Board.Board(self.boardSize)

        self.turn = "X"
        self.playGame()
    
    def gameSetup(self):
        success = 0
        while(not(success)):
            boardSize = input("Enter size of board (odd number): ")
            if (not(boardSize.isdigit())):
                print("Board size not a number")
            elif int(boardSize) < 3 or int(boardSize) % 2 == 0:   
                print("Number less than 3 or not odd")
            else:
                success = 1
        return int(boardSize)

    def gameDifficulty(self):
        success = 0
        while(not(success)):
            difficulty = input("Enter computer difficulty 1 (Easy), 2 (Medium), 3 (Hard): ")
            if (not(difficulty.isdigit())):
                print("Difficulty is not a number")
            elif int(difficulty) not in [1,2,3]:   
                print("Difficulty must be 1,2 or 3")
            else:
                success = 1
        return int(difficulty)
    
    def gameMode(self):
        success = 0
        while(not(success)):
            numPlayers = input("Enter 1 to play against computer or 2 to play between humans: ")
            if (not(numPlayers.isdigit())):
                print("Number of players is not a number")
            elif int(numPlayers) not in [1,2]:   
                print("Number of players must be 1 or 2")
            else:
                success = 1
        return int(numPlayers)

    def playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "X":
                self.getMoveHuman()
            else:
                self.getMoveCPU()

            self.board.takeTurn(self.X, self.Y, self.turn)
            self.board.printboard()

            gameEnd = self.board.checkGameEnd(self.turn)

            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def getMoveHuman(self):
        success = 0
        while (not(success)):
            userInput = input("Enter coordinates for " + self.turn + ": ")
            coordinates = userInput.split()

            if len(coordinates) != 2:
                print("You didnt enter 2 coordinates")
            else:
                X = coordinates[0]
                Y = coordinates[1]

                if (not(X.isdigit()) or int(X) >= self.boardSize):
                    print("First coordinate isnt an integer or less than " + str(self.boardSize))
                elif (not(Y.isdigit()) or int(Y) >= self.boardSize):
                    print("Second coordinate isnt an integer or less than " + str(self.boardSize))
                elif (not(self.board.validateTurn(int(X),int(Y),self.turn))):
                    print("Already move made at coordinates:" + str(coordinates))
                else:
                    self.X = int(X)
                    self.Y = int(Y)
                    success = 1 

    def getMoveCPU(self):
        if self.difficulty >= 1:
            move = self.board.makeMoveWin()
            self.X = move[0]
            self.Y = move[1]
        
        if (move[0] == self.boardSize):
            success = 0
            while (not(success)):
                X = random.randrange(self.boardSize)
                Y = random.randrange(self.boardSize)

                if (self.board.validateTurn(X,Y,self.turn)):
                    self.X = X
                    self.Y = Y
                    success = 1 


myTTT = TicTacToe()

