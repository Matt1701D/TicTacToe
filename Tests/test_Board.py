import unittest
import Board

class Test_Board(unittest.TestCase):
    def test_BoardSize(self):
        #Arrange
        myBoardSize = 3

        #Act
        myBoard = Board.Board(myBoardSize)
        myBoardData = myBoard.gameBoard[0]
        myBoardLength = len(myBoardData)
        
        #Assert
        self.assertEqual(myBoardLength,myBoardSize)
        self.assertEqual(myBoardData,['_']*3)

    def test_BoardMoveValid(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)

        #Act        
        myBoard.takeTurn(0,0,"X")
        
        #Assert
        self.assertEqual(myBoard.gameBoard[0],['X','_','_'])

    def test_BoardMoveInvalid(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")

        #Act        
        myBoard.takeTurn(0,0,"O")
        
        #Assert
        self.assertEqual(myBoard.gameBoard[0],['X','_','_'])

    def test_BoardMoveWinHorizontal(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(0,1,"X")

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[0,2])

    def test_BoardMoveWinVertical(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(1,0,"X")

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,0])

    def test_BoardMoveWinDiagonalRight(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(1,1,"X")

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,2])

    def test_BoardMoveWinDiagonalLeft(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,2,"X")
        myBoard.takeTurn(1,1,"X")

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,0])

    def test_BoardGameWinHorizontal(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(0,1,"X")
        myBoard.takeTurn(0,2,"X")

        #Act        
        result = myBoard.checkGameWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinVertical(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(1,0,"X")
        myBoard.takeTurn(2,0,"X")

        #Act        
        result = myBoard.checkGameWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinDiagonalRight(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,0,"X")
        myBoard.takeTurn(1,1,"X")
        myBoard.takeTurn(2,2,"X")

        #Act        
        result = myBoard.checkGameWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinDiagonalLeft(self):
        #Arrange
        myBoardSize = 3
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,2,"X")
        myBoard.takeTurn(1,1,"X")
        myBoard.takeTurn(2,0,"X")

        #Act        
        result = myBoard.checkGameWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardMoveCPUEasy(self):
        #Arrange
        myBoardSize = 3
        difficulty = 1
        turn = "X"
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,2,"X")
        myBoard.takeTurn(1,1,"X")

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        while(result == [2,0]):
            myBoard.gameBoard[2][0] = '_'
            result = myBoard.getMoveCPU(difficulty,turn)
        
        #Assert
        self.assertNotEqual(result,[2,0])

    def test_BoardMoveCPUHard2(self):
        #Arrange
        myBoardSize = 3
        difficulty = 3
        turn = "O"
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,2,"X")

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        myBoard.takeTurn(result[0],result[1],turn)
        
        #Assert
        self.assertEqual(myBoard.gameBoard[result[0]][result[1]],turn)

    def test_BoardMoveCPUHard(self):
        #Arrange
        myBoardSize = 3
        difficulty = 3
        turn = "X"
        myBoard = Board.Board(myBoardSize)
        myBoard.takeTurn(0,2,"X")
        myBoard.takeTurn(1,1,"X")

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        
        #Assert
        self.assertEqual(result,[2,0])

if __name__ == '__main__':
    unittest.main()
