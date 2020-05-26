from grid import Grid

class NoughtsAndCrosses():
    def __init__(self):
        #create grid
        self.grid = Grid(3, 3, ' ')
        self.char = 'x'

    def check_full(self):
        #check if the board is full
        #check every cell, if any are empty, return Flase
        for self.i in range(3):
            for self.a in range(3):
                if(self.grid.getCellValue(self.a,self.i)==' '):
                    return False
        return True

    def draw_grid(self):
        #draw the board
        print("\n\n%s|%s|%s\n-----\n%s|%s|%s\n-----\n%s|%s|%s\n" % (self.grid.getCellValue(0,0), self.grid.getCellValue(0,1), self.grid.getCellValue(0,2), self.grid.getCellValue(1,0), self.grid.getCellValue(1,1), self.grid.getCellValue(1,2), self.grid.getCellValue(2,0), self.grid.getCellValue(2,1), self.grid.getCellValue(2,2), ))

    def inputToGame(self, input_string):
        #split input into x coord and y coord
        input_list = input_string.split()
        print(input_list)

        #check that the cell is not already occupied
        if(self.grid.getCellValue(int(input_list[1]), int(input_list[0])) != ' '):
            print("Cell is already occupied.")
            return 0
        #check that the numbers are within the correct range
        if(int(input_list[0]) not in range(3) and int(input_list[1]) not in range(3)):
            print("Enter a number in the range 1 to 3.")
            return 0

        #set the value of the cell
        self.grid.setCellValue(int(input_list[1]), int(input_list[0]), self.char)

        #print current state of board
        self.draw_grid()

        #check if the victory condition is met
        #check rows
        for i in range(3):
            if(self.grid.getCellValue(0,i)==self.char and self.grid.getCellValue(1,i)==self.char and self.grid.getCellValue(2,i)==self.char):
                print("{} wins!".format(self.char))
                return -1
        #check columns
        for i in range(3):
            if(self.grid.getCellValue(i,0)==self.char and self.grid.getCellValue(i,1)==self.char and self.grid.getCellValue(i,2)==self.char):
                print("{} wins!".format(self.char))
                return -1
        #check diagonals
        if(self.grid.getCellValue(0,0)==self.char and self.grid.getCellValue(1,1)==self.char and self.grid.getCellValue(2,2)==self.char):
            print("{} wins!".format(self.char))
            return -1
        if(self.grid.getCellValue(0,2)==self.char and self.grid.getCellValue(1,1)==self.char and self.grid.getCellValue(2,0)==self.char):
            print("{} wins!".format(self.char))
            return -1

        #if the grid is full, end the game
        if(self.check_full()):
            print("Stalemate.")
            return -1

        #swap character for next player
        if(self.char == 'x'):
            self.char = 'o'
        else:
            self.char = 'x'

        #next player
        return 1

#for testing:
#game = NoughtsAndCrosses()
#gameState = 0
#while(gameState != -1):
    #gameState = game.inputToGame(input())
