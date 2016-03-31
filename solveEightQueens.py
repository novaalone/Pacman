import random
import copy
from optparse import OptionParser

class SolveEightQueens:
    def __init__(self, numberOfRuns, verbose, lectureExample):
        solutionCounter = 0
        lectureCase = [[]]
        if lectureExample:
            lectureCase = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "q", ".", ".", ".", "."],
            ["q", ".", ".", ".", "q", ".", ".", "."],
            [".", "q", ".", ".", ".", "q", ".", "q"],
            [".", ".", "q", ".", ".", ".", "q", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ]
        for i in range(0,numberOfRuns):
            if self.search(Board(lectureCase), verbose).getNumberOfAttacks() == 0:
                solutionCounter+=1
        print "Solved:",solutionCounter,"/",numberOfRuns

    def search(self, board, verbose):
        newBoard = board
        i = 0 
        while True:
            if verbose:
                print "iteration ",i
                print newBoard.toString()
                print newBoard.getCostBoard().toString()
            currentNumberOfAttacks = newBoard.getNumberOfAttacks()
            (newBoard, newNumberOfAttacks) = newBoard.getBetterBoard()
            i+=1
            if currentNumberOfAttacks <= newNumberOfAttacks:
                break
        return newBoard

class Board:
    def __init__(self, squareArray = [[]]):
        if squareArray == [[]]:
            self.squareArray = self.initBoardWithRandomQueens()
        else:
            self.squareArray = squareArray

    @staticmethod
    def initBoardWithRandomQueens():
        tmpSquareArray = [["." for i in range(0,8)] for j in range(0,8)]
        for i in range(0,8):
            tmpSquareArray[random.randint(0,7)][i] = "q"
        return tmpSquareArray
          
    def toString(self):
        s = ""
        for i in range(0,8):
            for j in range(0,8):
                s += str(self.squareArray[i][j]) + " "
            s += "\n"
        return s + "# attacks: "+str(self.getNumberOfAttacks())

    def getCostBoard(self):
        costBoard = copy.deepcopy(self)
        for r in range(0,8):
            for c in range(0,8):
                if self.squareArray[r][c] == "q":
                    for rr in range(0,8):
                        if rr!=r:
                            testboard = copy.deepcopy(self)
                            testboard.squareArray[r][c] = "."
                            testboard.squareArray[rr][c] = "q"
                            costBoard.squareArray[rr][c] = testboard.getNumberOfAttacks()
        return costBoard

    def getBetterBoard(self):
        #TODO: put your code here...
        currentAttack = self.getNumberOfAttacks()
        """
        start from the first column,move the queen along its column to get the minimal number of attack,
        then the second column,third column, until the last column
        """
        for c in range(0,8):
            for r in range(0,8):
                if self.squareArray[r][c]=='q':
                    for rr in range(0,8):
                        if rr!=r:
                            self.squareArray[rr][c]='q'
                            self.squareArray[r][c]='.'
                            newAttack = self.getNumberOfAttacks()
                            if newAttack<currentAttack:
                                return (self,newAttack)
                            else:
                                self.squareArray[rr][c]='.'
                                self.squareArray[r][c]='q'
                
        
                 
        return (self, 42)

    def getNumberOfAttacks(self):
        #TODO: put your code here...
        cost = 0
        for r in range(0,8):
            for c in range(0,8):
                if self.squareArray[r][c]=='q':
                    """ any attack in the same column? """
                    for rr in range(r+1,8):
                        if self.squareArray[rr][c]=='q':
                            cost+=1
                    """ any attack in the right down direction?"""
                    
                    cc=c+1
                    rr=r+1
                    while (cc<8 and rr<8):
                        if self.squareArray[rr][cc]=='q':
                            cost+=1
                        cc+=1
                        rr+=1
                    """any attck in the left down direction?"""
                    cc=c-1
                    rr=r+1
                    while (cc>=0 and rr<8):
                        if self.squareArray[rr][cc]=='q':
                            cost+=1
                        cc-=1
                        rr+=1
                    """ any attack in the same row?"""
                    for cc in range(c+1,8):
                        if self.squareArray[r][cc]=='q':
                            cost+=1
                            
        return cost

if __name__ == "__main__":
    #Enable the following line to generate the same random numbers (useful for debugging)
    #random.seed(0)
    parser = OptionParser()
    parser.add_option("-q", dest="verbose", action="store_false", default=True)
    parser.add_option("-l", dest="lectureExample", action="store_true", default=False)
    parser.add_option("-n", dest="numberOfRuns", default=1, type="int")
    (options, args) = parser.parse_args()
    SolveEightQueens(verbose=options.verbose, numberOfRuns=options.numberOfRuns, lectureExample=options.lectureExample)