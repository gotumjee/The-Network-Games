from grid import Grid

DIRECTIONS = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")

CHESS_PRINT = {
    "♔": "K",
    "♕": "Q",
    "♖": "R",
    "♗": "B",
    "♘": "N",
    "♙": "P",
    "♚": "k",
    "♛": "q",
    "♜": "r",
    "♝": "b",
    "♞": "n",
    "♟": "p"
}


def distance(x1, y1, x2, y2):
    """ Distance Function
    This function takes two co-ordinates from a square game board: (x1, y1) & (x2, y2)
    and finds the distance between them. The distance is based upon the number of cells
    between the two given cells, including the destination cell. If the two cells are not
    in a straight line, -1 is returned. If they are in a straight line, the distance is returned
    """
    x = abs(x1 - x2)
    y = abs(y1 - y2)

    if x == y:
        return x
    elif (x == 0) or (y == 0):
        return x+y
    else:
        return -1


def direction(x1, y1, x2, y2):
    """ Direction Function
    This function takes two co-ordinates from a square game board: (x1, y1) & (x2, y2)
    and finds the cardinal direction between them relative to (x1, y1). The direction is
    returned. Note that the function does not check that those directions which are not
    entirely north, south, east or west are exactly any other direction (for example NNW
    becomes NW).
    """
    line = ""
    if y1 > y2:
        line += "N"
    elif y1 < y2:
        line += "S"

    if x1 > x2:
        line += "W"
    elif x1 < x2:
        line += "E"

    return line


class Chess:
    """ The Chess Class
    This class a container for a game of chess and has two public
    classes: "printBoard" and "inputToGame".  All other classes are
    private and should not be accessed by code outside of the class.
    """

    def __init__(self, fill=None):
        # Create the board.
        self.fill = fill
        self.board = Grid(8, 8, fill)

        # 0 = White's turn, 1 = Black's turn
        self.turn = 0

        # [Left Rook, Right Rook, King] relative to the board
        self.blackCastling = [1, 1, 1]
        self.whiteCastling = [1, 1, 1]

        # Fill the board with pieces
        self.board.setYStripValues(1, "♟")
        self.board.setYStripValues(6, "♙")
        self.board.setYStripValues(0, ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"], 1)
        self.board.setYStripValues(7, ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"], 1)

    def printBoard(self):
        # Print the board.
        print("* │ a b c d e f g h\n──┼─────────────────")
        for y in range(8):
            print(str(y + 1) + " │", end=" ")
            for x in range(8):
                if self.board.getCellValue(x, y) is not None:
                    print(CHESS_PRINT[self.board.getCellValue(x, y)], end=" ")
                else:
                    print(". ", end="")
            print("")

    def inputToGame(self, stringIn):
        """ The inputToGame function
        The process for input to the game. Strings are inputted into the game
        and are used to play/control the states.
        """

        if stringIn.lower() == "r":
            # Choose to resign from the game.
            self.gameOver()
            return -1
        elif stringIn.lower() == "cl" and self.castlingCheck()[0] == 1:
            # Castle left (relative to the player's view)
            if self.turn == 0:
                self.board.swapTwo(4, 7, 2, 7)
                self.board.swapTwo(0, 7, 3, 7)
            else:
                self.board.swapTwo(4, 0, 2, 0)
                self.board.swapTwo(0, 0, 3, 0)
            return 1
        elif stringIn.lower() == "cr" and self.castlingCheck()[1] == 1:
            # Castle right (relative to the player's view)
            if self.turn == 0:
                self.board.swapTwo(4, 7, 6, 7)
                self.board.swapTwo(7, 7, 5, 7)
            else:
                self.board.swapTwo(4, 0, 6, 0)
                self.board.swapTwo(7, 0, 5, 0)
            return 1

        # Check each coordinate is valid
        for i in range(4):
            if (i % 2 == 0) and (stringIn[i] < "a" or stringIn[i] > "h"):
                return 0
            elif stringIn[i] < "1" or stringIn[i] > "8":
                return 0

        # Take each coordinate from input
        x1 = ord(stringIn[0]) - 97
        y1 = int(stringIn[1]) - 1
        x2 = int(stringIn[2]) - 97
        y2 = int(stringIn[3]) - 1

        if self.validMove(x1, y1, x2, y2) == 1:
            print("Move was valid! If your king is not in check")
            self.board.swapTwo(x1, y1, x2, y2)
            temp = self.board.getCellValue(x1, y1)
            self.board.setCellValue(x1, y1, self.fill)

            whiteCheck, blackCheck = self.checkForCheck()

            if (self.turn == 0 and whiteCheck == 1) or (self.turn == 0 and blackCheck == 1):
                print("You cannot put yourself into check.")
                self.board.setCellValue(x1, y1, temp)
                self.board.swapTwo(x1, y1, x2, y2)

                return 0
            else:
                if whiteCheck == 1 or blackCheck == 1:
                    print("Check!")
                self.turn = (self.turn + 1) % 2  # Alternates self.turn between 0 and 1. #
                self.pawnPromote()

                # Tracking which rooks have moved (for Castling)
                if x1 == 0 and y1 == 0:
                    self.blackCastling[0] = 0
                elif x1 == 7 and y1 == 0:
                    self.blackCastling[1] = 0
                elif x1 == 0 and y1 == 7:
                    self.whiteCastling[0] = 0
                elif x1 == 7 and y1 == 7:
                    self.whiteCastling[1] = 0

                # Tracking which kings have moved
                elif x1 == 4 and y1 == 0:
                    self.blackCastling[2] = 0
                elif x1 == 4 and y1 == 7:
                    self.whiteCastling[2] = 0

                return 1

        else:
            return 0

    # Find the closest (if any) piece in a given direction from another piece
    def findInterceptPiece(self, x, y, line):
        print("findInterceptPiece being run!\nx="+str(x)+", y="+str(y)+", line = "+line)
        xStep = 0
        yStep = 0

        if "N" in line:
            yStep = -1
        if "S" in line:
            yStep = 1
        if "E" in line:
            xStep = 1
        if "W" in line:
            xStep = -1

        x += xStep
        y += yStep
        distanceAway = 1

        while (x in range(8)) and (y in range(8)):
            if self.board.getCellValue(x, y) != self.fill:
                print("distanceAway="+str(distanceAway))
                return distanceAway, self.getPieceNumber(x, y)
            x += xStep
            y += yStep
            distanceAway += 1

        return -1, -1

    # Checking a move is valid. Returns boolean
    def validMove(self, x1, y1, x2, y2):
        print("validMove has been executed")
        # Check that the coordinates differ
        if x1 == x2 and y1 == y2:
            print("x1 == x2, y1 == y2")
            return 0

        if self.fill is None:
            fill = -1
        else:
            fill = ord(self.fill)

        # Get the items at the coordinates
        piece = self.getPieceNumber(x1, y1)
        print(piece)
        dest = self.getPieceNumber(x2, y2)

        if piece == -1:
            print("Piece location is empty")
            return 0

        # Check whether the correct colour of piece is trying to move. Also check that if a piece would be taken,
        # it is not their own piece:
        # White Piece
        print(piece, self.turn, dest)
        if 9812 <= piece <= 9817 and (self.turn == 1 or (9812 <= dest <= 9817)):
            print("The piece is white and (it's black's turn or you'd be taking a white piece)")
            return 0
        # Black Piece
        elif 9818 <= piece <= 9823 and (self.turn == 0 or (9812 <= dest <= 9817)):
            print("The piece is black and (it's white's turn or you'd be taking a black piece)")
            return 0

        # Check whether the piece can get to its destination
        if piece == 9812 or piece == 9818:
            print("It's a king")
            # King
            # Check the movement has a distance of only 1
            if distance(x1, y1, x2, y2) == 1:

                # Check the two kings will still be at least two spaces away from each other
                if self.turn == 0:
                    x, y = self.board.findPiece("♚")
                else:
                    x, y = self.board.findPiece("♔")

                if distance(x2, y2, x, y) > 2:
                    return 1

            return 0

        elif piece == 9813 or piece == 9819:
            # The piece is a queen
            print("It's a queen")
            # Check the movement is a straight line in some direction.
            if (x1 == x2) or (y1 == y2) or ((x2-x1) == (y2-y1)):
                # Find which straight line needs to be checked for pieces.
                line = direction(x1, y1, x2, y2)

                # Ensure there is no piece blocking the path of the queen.
                if distance(x1, y1, x2, y2) <= self.findInterceptPiece(x1, y1, line)[0]:
                    return 1

            return 0

        elif piece == 9814 or piece == 9820:
            # The piece is a rook.
            print("It's a rook")

            # Check the movement is either north, south, east or west
            # (i.e. not diagonal).
            if (x1 == x2) or (y1 == y2):
                line = direction(x1, y1, x2, y2)

                # Ensure there is no piece blocking the path of the rook.
                if distance(x1, y1, x2, y2) <= self.findInterceptPiece(x1, y1, line)[0]:
                    return 1

            return 0

        elif piece == 9815 or piece == 9821:
            # The piece is a bishop.
            print("It's a bishop")

            # Check the movement is diagonal.
            if (x2-x1) == (y2-y1):
                # Find which diagonal line
                line = direction(x1, y1, x2, y2)

                # Ensure there is no piece blocking the path of the bishop
                if distance(x1, y1, x2, y2) <= self.findInterceptPiece(x1, y1, line)[0]:
                    return 1

            return 0

        elif piece == 9816 or piece == 9822:
            # Knight
            print("It's a knight")
            # Check the movement is value (2 in one, 1 in another)
            if (abs(x2-x1) == 1 and abs(y2-y1) == 2) or (abs(x2-x1) == 2 and abs(y2-y1) == 1):
                return 1

            return 0

        elif piece == 9817 or piece == 9823:
            # Pawn
            print("It's a pawn")
            # Check the movement is only one square
            if distance(x1, y1, x2, y2) == 1:
                if piece == 9817:
                    # White
                    if x1 == x2 and y1-1 == y2:
                        # Move forward
                        if dest == -1:
                            return 1
                    elif abs(x2-x1) == 1 and y1-1 == y2:
                        # Take a piece if it is black
                        if 9818 <= dest <= 9823:
                            return 1

                else:
                    # Black
                    if x1 == x2 and y1+1 == y2:
                        # Move forward
                        if dest == -1:
                            return 1
                    elif abs(x2-x1) == 1 and y1+1 == y2:
                        # Take a piece if it is white
                        if 9818 <= dest <= 9823:
                            return 1

            # Check the piece hasn't moved yet
            elif distance(x1, y1, x2, y2) == 2:
                # White
                if piece == 9817 and y1 == 6:
                    if x1 == x2 and y1-2 == y2 and self.getPieceNumber(x1, y1-1) == dest == fill:
                        return 1
                # Black
                elif y1 == 1:
                    if x1 == x2 and y1+2 == y2 and self.getPieceNumber(x1, y1+1) == dest == fill:
                        return 1

            else:
                return 0

        else:
            # No Piece Specified
            print("It's nothing?")
            return 0

        print("Somethings wrong")
        return 0

    def getPieceNumber(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return -1
        elif self.board.getCellValue(x, y) is None:
            return -1
        else:
            return ord(self.board.getCellValue(x, y))

    def checkForCheck(self):
        """The checkForCheck function.

        This function is used to determine whether either (or both)
        kings are in check.
        Each cardinal direction is checked to find which (if any)
        is closest in that line.  If the piece is owned by the
        opponent and could take the king if it were to move, the
        king is in check.
        Next, the locations that a knight could be located are
        checked for knights of the opposing colour.  If they exist,
        the king is in check.
        """
        whiteCheck = False
        blackCheck = False

        # White
        x, y = self.board.findPiece("♔")
        for line in DIRECTIONS:
            distanceAway, piece = self.findInterceptPiece(x, y, line)
            if piece == 9819:
                # In path of black queen
                whiteCheck = True
                break

            elif line in ["N", "E", "S", "W"] and piece == 9820:
                # In path of black rook
                whiteCheck = True
                break

            elif line in ["SE", "SW"] and piece == 9821:
                # In path of black bishop
                whiteCheck = True
                break

            elif line in ["NE", "NW"]:
                if piece == 9821:
                    # In path of black bishop
                    whiteCheck = True
                    break

                if piece == 9823 and distanceAway == 1:
                    # In path of black pawn
                    whiteCheck = True
                    break

        if whiteCheck is False:
            for kx in [-2, -1, 1, 2]:
                for ky in [-2, -1, 1, 2]:
                    if abs(kx) == abs(ky):
                        continue

                    if self.getPieceNumber(x+kx, y+ky) == 9822:
                        # In the path of black knight
                        whiteCheck = True
                        break

                else:  # https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops #
                    continue
                break

        # Black
        x, y = self.board.findPiece("♚")
        for line in DIRECTIONS:
            distanceAway, piece = self.findInterceptPiece(x, y, line)
            if piece == 9813:
                # In path of white queen
                blackCheck = True
                break

            elif line in ["N", "E", "S", "W"] and piece == 9814:
                # In path of white rook
                blackCheck = True
                break

            elif line in ["NE", "NW"] and piece == 9815:
                # In path of white bishop
                blackCheck = True
                break

            elif line in ["SE", "SW"]:
                if piece == 9815:
                    # In path of white bishop
                    blackCheck = True
                    break

                if piece == 9817 and distanceAway == 1:
                    # In path of white pawn
                    blackCheck = True
                    break

        if blackCheck is False:
            for kx in [-2, -1, 1, 2]:
                for ky in [-2, -1, 1, 2]:
                    if abs(x) == abs(y):
                        continue

                    if self.getPieceNumber(x+kx, y+ky) == 9816:
                        # In the path of black knight
                        blackCheck = True
                        break

                else:  # https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops #
                    continue
                break

        return whiteCheck, blackCheck

    def pawnPromote(self):
        for whiteBlack in [(0, 9817, "♕"), (7, 9823, "♛")]:
            for x in range(8):
                if self.getPieceNumber(x, whiteBlack[0]) == whiteBlack[1]:
                    self.board.setCellValue(x, whiteBlack[0], whiteBlack[2])

    def castlingCheck(self):

        # Check which players turn it is
        if self.turn == 0:
            # White
            # Rule 1/2: Neither the rook or king has moved
            if self.whiteCastling[2] == 0:
                return 0, 0
            left, right = self.whiteCastling[0], self.whiteCastling[1]

            # Rule 4: The king is not in check
            if self.checkForCheck()[0] == 1:
                return 0, 0

            # Rule 3: There are no pieces between the king and the rook
            if not self.getPieceNumber(1, 7) == self.getPieceNumber(2, 7) == self.getPieceNumber(3, 7) == -1:
                left = 0
            if not self.getPieceNumber(5, 7) == self.getPieceNumber(6, 7) == -1:
                right = 0

            # Rule 5/6: The king does not move through or into check
            swaps = (((2, 7), (3, 7)),
                     ((5, 7), (6, 7))
                     )

            for leftRight in range(1):
                for xy in swaps[leftRight]:
                    self.board.swapTwo(xy[0], xy[1], 4, 7)

                    if self.checkForCheck()[0] == 1:
                        if leftRight == 0:
                            left = 0
                        else:
                            right = 0

                    self.board.swapTwo(xy[0], xy[1], 4, 7)

            return left, right

        else:
            # Black
            # Rule 1/2: Neither the rook or king has moved
            if self.blackCastling[2] == 0:
                return 0, 0
            left, right = self.blackCastling[0], self.blackCastling[1]

            # Rule 4: The king is not in check
            if self.checkForCheck()[1] == 1:
                return 0, 0

            # Rule 3: There are no pieces between the king and the rook
            if not self.getPieceNumber(1, 0) == self.getPieceNumber(2, 0) == self.getPieceNumber(3, 0) == -1:
                left = 0
            if not self.getPieceNumber(5, 0) == self.getPieceNumber(6, 0) == -1:
                right = 0

            # Rule 5/6: The king does not move through or into check
            swaps = (((2, 0), (3, 0)),
                     ((5, 0), (6, 0))
                     )

            for leftRight in range(1):
                for xy in swaps[leftRight]:
                    self.board.swapTwo(xy[0], xy[1], 4, 0)

                    if self.checkForCheck()[1] == 1:
                        if leftRight == 0:
                            left = 0
                        else:
                            right = 0

                    self.board.swapTwo(xy[0], xy[1], 4, 0)

            return left, right

    def gameOver(self):
        whiteCheck, blackCheck = self.checkForCheck()

        if self.turn == 1 and blackCheck == 1:
            print("White wins!")
        elif self.turn == 0 and whiteCheck == 1:
            print("Black wins!")
        else:
            print("Stalemate or Resignation! No winner.")

def main():
    a = Chess()
    while True:
        a.printBoard()
        a.inputToGame(input(""))


if __name__ == "__main__":
    main()
