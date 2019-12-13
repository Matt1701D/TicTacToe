import random

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
        if self.validateTurn(X,Y,turn):
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
        XCountR = OCountR = BCountR = 0
        XCountL = OCountL = BCountL = 0

        for i in range(self.boardSize):
            #check horizontal
            if (self.gameBoard[i].count('_') == 1 and (self.gameBoard[i].count('O') == self.boardSize - 1 or (self.gameBoard[i].count('X') == self.boardSize - 1))):
                X = i
                Y = self.gameBoard[i].index('_')

            #check vertical
            if (self.gameBoardTranspose[i].count('_') == 1 and (self.gameBoardTranspose[i].count('O') == self.boardSize - 1 or (self.gameBoardTranspose[i].count('X') == self.boardSize - 1))):
                X = self.gameBoardTranspose[i].index('_')
                Y = i

            #check diagonal right
            if self.gameBoard[i][i] == 'X':
                XCountR += 1
            elif self.gameBoard[i][i] == 'O':
                OCountR += 1
            else:
                BlankR = [i, i]
                BCountR += 1

            #check diagonal left
            XCoord = self.boardSize - 1 - i
            if self.gameBoard[XCoord][i] == 'X':
                XCountL += 1
            elif self.gameBoard[XCoord][i] == 'O':
                OCountL += 1
            else:
                BlankL = [XCoord, i]
                BCountL += 1

        if BCountR == 1 and ((XCountR == self.boardSize - 1) or (OCountR == self.boardSize - 1)):
            X = BlankR[0]
            Y = BlankR[1]
        elif BCountL == 1 and ((XCountL == self.boardSize - 1) or (OCountL == self.boardSize - 1)):
            X = BlankL[0]
            Y = BlankL[1]

        return [X,Y]

    def getMoveCPU(self,difficulty,turn):
        if difficulty >= 2:
            move = self.makeMoveWin()

        if difficulty == 1 or move[0] == self.boardSize:
            X = random.randrange(self.boardSize)
            Y = random.randrange(self.boardSize)
            while (not(self.validateTurn(X,Y,turn))):
                X = random.randrange(self.boardSize)
                Y = random.randrange(self.boardSize)
            move = [X,Y]

        return move

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