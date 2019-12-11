
class TicTacToe:

    def __init__(self):
        self.boardSize = self.gameSetup()
        self.numPlayers = self.gameMode()
        self.difficulty = 0 if self.numPlayers == 1 else self.gameDifficulty()
        self.board = Board(self.boardSize)
        
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
        return difficulty
    
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
        return numPlayers

    def play():
        if self.numPlayers == 2:
            self.playGame()

    def playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            self.getMove()
            self.board.takeTurn(self.X, self.Y, self.turn)
            self.board.printboard()

            gameEnd = self.board.checkGameEnd(self.turn)

            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def getMove(self):
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

class Board:
    turnsTaken = 0

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.initBoard()

    def initBoard(self):
        self.gameBoard = [['_'] * self.boardSize for x in range(self.boardSize)]

    def validateTurn(self,X,Y,turn):
        return self.gameBoard[X][Y] == '_'

    def takeTurn(self,X,Y,turn):
        self.gameBoard[X][Y] = turn
        self.turnsTaken+=1

    def checkGameWinner(self):
        sofarR = 1
        sofarL = 1
        sofarV = 1

        for i in range(self.boardSize):
            #check horizontal
            if (self.gameBoard[i] == ['X']*self.boardSize or self.gameBoard[i] == ['O']*self.boardSize):
                return 1

            #check vertical
            for j in range(self.boardSize - 1):
                if sofarV:
                    sofarV =  (self.gameBoard[j][i] == self.gameBoard[j+1][i]) and (self.gameBoard[j][i] in ['X','O'])
            if sofarV:
                return 1
            else:
                sofarV = 1

            #check diagonal right and left
            if sofarR and i != self.boardSize - 1:
                sofarR = (self.gameBoard[i][i] == self.gameBoard[i+1][i+1]) and (self.gameBoard[i][i] in ['X','O'])

            if sofarL and i != self.boardSize - 1:
                XCoord = self.boardSize - 1 - i
                sofarL = (self.gameBoard[XCoord][i] == self.gameBoard[XCoord-1][i+1]) and (self.gameBoard[XCoord][i] in ['X','O'])

        if sofarR or sofarL:
            return 1
        else:
            return 0

    def checkGameEnd(self, turn):
        if self.turnsTaken == self.boardSize * self.boardSize:
            print("DRAW!")
            return 1
        elif self.checkGameWinner():
            print(str(turn) + " WINS!")
            return 1
        else:
            return 0

    def printboard(self):
        for row in self.gameBoard:
            print(' '.join([str(s) for s in row]))

myTTT = TicTacToe()

