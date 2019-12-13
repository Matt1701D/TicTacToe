class Board:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.__turnsTaken = 0
        self.initBoard()

    def initBoard(self):
        self.gameBoard = [['_'] * self.boardSize for x in range(self.boardSize)]
        self.gameBoardTranspose = [['_'] * self.boardSize for x in range(self.boardSize)]

    def validateTurn(self,X,Y,turn):
        return self.gameBoard[X][Y] == '_'

    def takeTurn(self,X,Y,turn):
        self.gameBoard[X][Y] = turn
        self.gameBoardTranspose[Y][X] = turn
        self.__turnsTaken+=1

    def checkGameWinner(self):
        sofarR = 1
        sofarL = 1
        sofarV = 1

        for i in range(self.boardSize):
            #check horizontal
            if (self.gameBoard[i] == ['X']*self.boardSize or self.gameBoard[i] == ['O']*self.boardSize):
                return 1

            #check vertical
            if (self.gameBoardTranspose[i] == ['X']*self.boardSize or self.gameBoardTranspose[i] == ['O']*self.boardSize):
                return 1

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

    def makeMoveWin(self):
        X = Y = self.boardSize
        XCount = OCount = BCount = 0

        for i in range(self.boardSize):
            #check horizontal
            if (self.gameBoard[i].count('_') == 1 and (self.gameBoard[i].count('O') == self.boardSize - 1 or (self.gameBoard[i].count('X') == self.boardSize - 1))):
                X = i
                Y = self.gameBoard[i].index('_')

            #check vertical
            if (self.gameBoardTranspose[i].count('_') == 1 and (self.gameBoardTranspose[i].count('O') == self.boardSize - 1 or (self.gameBoardTranspose[i].count('X') == self.boardSize - 1))):
                X = self.gameBoardTranspose[i].index('_')
                Y = i

            #check diagonal
            if self.gameBoard[i][i] == 'X':
                XCount += 1
            elif self.gameBoard[i][i] == 'O':
                OCount += 1
            else:
                Blank = [i, i]
                BCount += 1

        if BCount == 1 and ((XCount == self.boardSize - 1) or (OCount == self.boardSize - 1)):
            X = Blank[0]
            Y = Blank[1]

        return [X,Y]

    def checkGameEnd(self, turn):
        if self.__turnsTaken == self.boardSize * self.boardSize:
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
        print("\n")