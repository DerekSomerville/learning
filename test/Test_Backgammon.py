import blackgammon
import unittest
import copy

class Test_BackGammon(unittest.TestCase):
    white = "white"
    black = "black"

    currentBoard = [[black,0],
        [black,2],[None,0],[black,2],[None,0],[None,0],[black,3],[None,0],[black,1],[None,0],[None,0],[None,0],[white,5],
        [black,5],[None,0],[None,0],[None,0],[white,2],[None,0],[white,5],[None,0],[None,0],[white,1],[None,0],[black,2],
        [white,0],
        [white,1],
        [black,0]]

    def test_throwADie(self):
        die = blackgammon.throwADie()
        self.assertTrue(die >= 1 and die <= 6)

    def test_MoveFromMiddleWhite(self):
        self.assertEqual(1,blackgammon.determineNewPosition(self.white,26,1))

    def test_MoveFromMiddleBlack(self):
        self.assertEqual(24,blackgammon.determineNewPosition(self.black,27,1))

    def test_determinNewPositionWhite(self):
        self.assertEqual(7,blackgammon.determineNewPosition(self.white,1,6))

    def test_determinNewPositionWhiteMiddle(self):
        self.assertEqual(4,blackgammon.determineNewPosition(self.white,26,4))

    def test_determinNewPositionWhiteMiddle2(self):
        self.assertEqual(6,blackgammon.determineNewPosition(self.white,26,6))

    def test_determinNewPositionBlack(self):
        self.assertEqual(7,blackgammon.determineNewPosition(self.black,8,1))

    def test_dieExists(self):
        self.assertTrue(blackgammon.dieExists([2,3],3))

    def test_dieExistsFalse(self):
        self.assertFalse(blackgammon.dieExists([2,3],4))

    def test_validatePointToMoveFromWhiteMiddle(self):
        self.assertTrue(blackgammon.validatePointToMoveFrom(self.currentBoard,self.white,26,True))

    def test_validatePointToMoveFromWhiteWithMiddle(self):
        self.assertFalse(blackgammon.validatePointToMoveFrom(self.currentBoard,self.white,12,True))

    def test_validatePointToMoveFromBlack(self):
        self.assertTrue(blackgammon.validatePointToMoveFrom(self.currentBoard,self.black,13,True))

    def test_validatePointToMoveToNone(self):
        self.assertTrue(blackgammon.validatePointToMoveTo(self.currentBoard,self.black,7,True))

    def test_validatePointToMoveToSameColour(self):
        self.assertTrue(blackgammon.validatePointToMoveTo(self.currentBoard,self.black,8,True))

    def test_validatePointToMoveToHasDifferentColour(self):
        self.assertFalse(blackgammon.validatePointToMoveTo(self.currentBoard,self.white,1,True))

    def test_validatePointToMoveToOtherColourOne(self):
        self.assertTrue(blackgammon.validatePointToMoveTo(self.currentBoard,self.black,22,False))

    def test_validatePointToMoveToOtherColour(self):
        self.assertFalse(blackgammon.validatePointToMoveTo(self.currentBoard,self.black,19,True))

    def test_validatePointToMoveToFromMiddle(self):
        currentBoard = [[self.black,0],
            [self.black,1],[self.white,2],[self.black,2],[self.white,2],[self.black,2],[self.black,2],[None,0],[self.black,1],[None,0],[None,0],[self.black,2],[self.white,2],
            [None,0],[None,0],[None,0],[None,0],[None,0],[self.white,1],[self.white,2],[self.black,1],[None,0],[self.white,1],[self.white,3],[self.black,2],
            [self.white,0],
            [self.white,0],
            [self.black,0]]
        self.assertFalse(blackgammon.validatePointToMoveTo(self.currentBoard,self.white,3,True))

    def test_makePlayerMove(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,0],
            [self.black,0]]
        blackgammon.makePlayerMove(currentBoard,self.black,24,2)
        self.assertEqual(currentBoard[22],[self.black,1])

    def test_makePlayerMoveToSameColour(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,0],
            [self.black,0]]
        blackgammon.makePlayerMove(currentBoard,self.black,8,1)
        self.assertEqual(currentBoard[7],[self.black,2])

    def test_makePlayerMoveMoveToMiddle(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[self.black,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,0],
            [self.black,0]]
        blackgammon.makePlayerMove(currentBoard,self.black,16,1)
        self.assertEqual(currentBoard[15],[self.black,1])
        self.assertEqual(currentBoard[26],[self.white,1])


    def test_validatePointToMoveFrom(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[self.black,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,1],
            [self.black,0]]
        self.assertFalse(blackgammon.validatePointToMoveFrom(currentBoard,self.white,12,True))

    def test_validPlayerInstructions(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[self.black,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,1],
            [self.black,0]]
        self.assertFalse(blackgammon.validPlayerInstructions(currentBoard,self.white,[2,3],12,2,True))

    def test_playerCanMove(self):
        currentBoard = [[self.black,0],
            [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,1],[self.black,2],[None,0],[None,0],[None,0],[self.white,1],
            [None,0],[self.white,3],[self.white,1],[self.black,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.black,1],
            [self.white,0],
            [self.white,1],
            [self.black,0]]
        self.assertFalse(blackgammon.playerCanMove(currentBoard,self.white,[2,3]))

    def test_allInHomeNot(self):
        self.assertFalse(blackgammon.allInHome(self.currentBoard,self.black))

    def test_allInHomeNearly(self):
        currentBoard = [[self.black,0],
                [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,4],[self.black,1],[None,0],[None,0],[None,0],[None,0],[self.white,1],
                [None,0],[self.white,3],[self.white,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.white,4],
                [self.white,0],
                [self.white,1],
                [self.black,0]]
        self.assertFalse(blackgammon.allInHome(currentBoard,self.black))

    def test_allInHomeBlack(self):
        currentBoard = [[self.black,0],
                [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,5],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,1],
                [None,0],[self.white,3],[self.white,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.white,4],
                [self.white,0],
                [self.white,1],
                [self.black,0]]
        self.assertTrue(blackgammon.allInHome(currentBoard,self.black))

    def test_allInHomeWhiteNotAll(self):
        currentBoard = [[self.black,0],
                [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,5],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,1],
                [None,0],[self.white,3],[self.white,1],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,4],[self.white,4],
                [self.white,0],
                [self.white,1],
                [self.black,0]]
        self.assertFalse(blackgammon.allInHome(currentBoard,self.white))

    def test_allInHomeWhite(self):
        currentBoard = [[self.black,0],
                [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,5],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],
                [None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,5],[self.white,5],[self.white,5],
                [self.white,0],
                [self.white,0],
                [self.black,0]]
        self.assertTrue(blackgammon.allInHome(currentBoard,self.white))

    def test_allInHomeWhiteWithHome(self):
        currentBoard = [[self.black,0],
                [self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,2],[self.black,5],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],
                [None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[self.white,5],[self.white,3],[self.white,5],
                [self.white,2],
                [self.white,0],
                [self.black,0]]
        self.assertTrue(blackgammon.allInHome(currentBoard,self.white))

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
