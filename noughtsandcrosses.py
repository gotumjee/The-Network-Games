from grid import Grid


class NoughtsAndCrosses:
    def __init__(self):
        # Create grid
        self.grid = Grid(3, 3, ' ')
        self.char = 'x'

    def check_full(self):
        # Check if the board is full
        # Check every cell, if any are empty, return False
        for self.i in range(3):
            for self.a in range(3):
                if self.grid.getCellValue(self.a, self.i) == ' ':
                    return False
        return True

    def draw_grid(self):
        # Draw the board
        print("\n\n%s|%s|%s\n-----\n%s|%s|%s\n-----\n%s|%s|%s\n" %
              (self.grid.getCellValue(0, 0), self.grid.getCellValue(0, 1), self.grid.getCellValue(0, 2),
               self.grid.getCellValue(1, 0), self.grid.getCellValue(1, 1), self.grid.getCellValue(1, 2),
               self.grid.getCellValue(2, 0), self.grid.getCellValue(2, 1), self.grid.getCellValue(2, 2))
              )

    def inputToGame(self, input_string):
        # Split input into x coord and y coord
        input_list = input_string.split()

        if len(input_list) != 2:
            print("Please enter coordinates in the form \"x y\".")
            return 0

        # Check that the numbers are within the correct range
        if int(input_list[0]) not in range(3) and int(input_list[1]) not in range(3):
            print("Enter a number in the range 0 to 2.")
            return 0

        # Check that the cell is not already occupied
        if self.grid.getCellValue(int(input_list[1]), int(input_list[0])) != ' ':
            print("Cell is already occupied.")
            return 0

        # Set the value of the cell
        self.grid.setCellValue(int(input_list[1]), int(input_list[0]), self.char)

        # Print current state of board
        self.draw_grid()

        # Check if the victory condition is met
        # Check rows
        for i in range(3):
            if (self.grid.getCellValue(0, i) == self.grid.getCellValue(1, i)
                    == self.grid.getCellValue(2, i) == self.char):
                print("{} wins!".format(self.char))
                return -1
        # Check columns
        for i in range(3):
            if (self.grid.getCellValue(i, 0) == self.grid.getCellValue(i, 1)
                    == self.grid.getCellValue(i, 2) == self.char):
                print("{} wins!".format(self.char))
                return -1
        # Check diagonals
        if self.grid.getCellValue(0, 0) == self.grid.getCellValue(1, 1) == self.grid.getCellValue(2, 2) == self.char:
            print("{} wins!".format(self.char))
            return -1
        if self.grid.getCellValue(0, 2) == self.grid.getCellValue(1, 1) == self.grid.getCellValue(2, 0) == self.char:
            print("{} wins!".format(self.char))
            return -1

        # If the grid is full, end the game
        if self.check_full():
            print("Stalemate.")
            return -1

        # Swap character for next player
        if self.char == 'x':
            self.char = 'o'
        else:
            self.char = 'x'

        # Next player
        return 1

# For testing:
# game = NoughtsAndCrosses()
# gameState = 0
# while gameState != -1:
#     gameState = game.inputToGame(input())
