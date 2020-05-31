class Battleships:
    __boardSetup = 1
    __usr = None
    __count = 1
    __turn = 0
    __firstWin = 0

    # initializes the "boards" with value '0'
    __p1_board = [[0] * 10 for _ in range(10)]
    __p2_board = [[0] * 10 for _ in range(10)]
    __p1_play = [[0] * 10 for _ in range(10)]
    __p2_play = [[0] * 10 for _ in range(10)]

    # used to ensure that each ships down message only prints once
    __u1ret1 = 0
    __u1ret2 = 0
    __u1ret3 = 0
    __u1ret4 = 0
    __u1ret5 = 0

    __u2ret1 = 0
    __u2ret2 = 0
    __u2ret3 = 0
    __u2ret4 = 0
    __u2ret5 = 0

    def __init__(self, usr):
        # defines the User based on the user number passed by the main program
        if usr == 1:
            self.__usr = 1

        elif usr == 2:
            self.__usr = 2

        else:
            raise Exception("Invalid input;  please enter 1 or 2..\n")

    def __conversion(self, board, row, column):
        # since the program uses numbers, this function converts the numbers to
        # make sense to the user
        if board[row][column] == 0:
            return str(' ')

        elif board[row][column] == 1:
            return str('C')

        elif board[row][column] == 2:
            return str('B')

        elif board[row][column] == 3:
            return str('D')

        elif board[row][column] == 4:
            return str('S')

        elif board[row][column] == 5:
            return str('P')

        elif board[row][column] == 6:
            return str('$')

        elif board[row][column] == 7:
            return str('*')

    def display(self, board=[[0] * 10 for _ in range(10)]):
        # used to display the board with the necessary formatting
        row = 0  # represents each rows
        # prints the line numbers horizontally
        print("\n     1   2   3   4   5   6   7   8   9   10")

        for i in range(21):
            if i % 2 == 0:
                print("   +---+---+---+---+---+---+---+---+---+---+",
                      end='\n')  # prints the border for the grid

            else:  # prints the line number vertically with appropriate spacing
                if((i // 2) + 1) != 10:
                    print(str((i // 2) + 1), end="  ")

                else:
                    print(str((i // 2) + 1), end=' ')

                column = 0  # represents each element horizontally
                for _ in range(10):
                    # prints the ships to the screen (using the conversion()
                    # function) with appropriate borders and spacing
                    print(
                        "| " +
                        self.__conversion(
                            board,
                            row,
                            column),
                        end=' ')
                    column += 1  # increments column to move to the next element

                print('|')
                row += 1  # moves to the next row

        return

    def __shipsplace(self, row, column, orientation):
        # used to place the ships based off inputs provided by the user
        if self.__usr == 1 and self.__boardSetup == 1:

            self.__boardSetup = 2
            if self.__count == 1:

                print("Placing Carrier ships now")
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'C') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("The ships have been placed.\n")
                self.display(self.__p1_board)
                self.__count += 1
                return 0

            elif self.__count == 3:

                print("Placing Battleships now")
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'B') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("The ships have been placed.\n")
                self.display(self.__p1_board)
                self.__count += 1
                return 0

            elif self.__count == 5:

                print("Placing Destroyer ships now")
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'D') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("The ships have been placed.\n")
                self.display(self.__p1_board)
                self.__count += 1
                return 0

            elif self.__count == 7:

                print("Placing Submarines now")
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'S') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("The ships have been placed.\n")
                self.display(self.__p1_board)
                self.__count += 1
                return 0

            elif self.__count == 9:

                print("Placing Patrol boats now")
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'P') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("The ships have been placed.\n")
                self.display(self.__p1_board)
                self.__count += 1

                self.__boardSetup = 2
                print("\nDone placing ships!\nYour opponent will place ships now.")
                return 0

        if self.__usr == 2 and self.__boardSetup == 1:

            self.__boardSetup = 2
            if self.__count == 1:
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'C') == 0:
                    return -1

                print("Your opponent has placed their Carrier ships.")
                self.__count += 1
                return 0

            elif self.__count == 3:
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'B') == 0:
                    return -1

                print("Your opponent has placed their Battleships.")
                self.__count += 1
                return 0

            elif self.__count == 5:
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'D') == 0:
                    return -1

                print("Your opponent has placed their Destroyer ships.")
                self.__count += 1
                return 0

            elif self.__count == 7:
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'S') == 0:
                    return -1

                print("Your opponent has placed their Submarines.")
                self.__count += 1
                return 0

            elif self.__count == 9:
                if self.__placement(
                        self.__p1_board,
                        row,
                        column,
                        orientation,
                        'P') == 0:
                    return -1

                print("Your opponent has placed their Patrol boats.")
                self.__count += 1

                self.__boardSetup = 2
                print("Your opponent is done placing ships!")
                return 0

        if self.__usr == 2 and self.__boardSetup == 2:

            self.__boardSetup = 1
            if self.__count == 2:

                print("Placing Carrier ships now")
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'C') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("\nThe ships have been placed.")
                self.display(self.__p2_board)
                self.__count += 1
                return 0

            elif self.__count == 4:

                print("Placing Battleships now")
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'B') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("\nThe ships have been placed.")
                self.display(self.__p2_board)
                self.__count += 1
                return 0

            elif self.__count == 6:

                print("Placing Destroyer ships now")
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'D') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("\nThe ships have been placed.")
                self.display(self.__p2_board)
                self.__count += 1
                return 0

            elif self.__count == 8:

                print("Placing Submarines now")
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'S') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("\nThe ships have been placed.")
                self.display(self.__p2_board)
                self.__count += 1
                return 0

            elif self.__count == 10:

                print("Placing Patrol boats now")
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'P') == 0:
                    print(
                        "\nThe ships could not be placed..\nPlease check the board and try again.")
                    return -1

                print("\nThe ships have been placed.")
                self.display(self.__p2_board)
                self.__count += 1

                self.__boardSetup = 0
                self.__turn = 1
                print("\nDone placing ships!\nThe game will start now.")
                return 0

        if self.__usr == 1 and self.__boardSetup == 2:

            self.__boardSetup = 1
            if self.__count == 2:
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'C') == 0:
                    return -1

                print("Your opponent has placed their Carrier ships.")
                self.__count += 1
                return 0

            elif self.__count == 4:
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'B') == 0:
                    return -1

                print("Your opponent has placed their Battleships.")
                self.__count += 1
                return 0

            elif self.__count == 6:
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'D') == 0:
                    return -1

                print("Your opponent has placed their Destroyer ships.")
                self.__count += 1
                return 0

            elif self.__count == 8:
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'S') == 0:
                    return -1

                print("Your opponent has placed their Submarines.")
                self.__count += 1
                return 0

            elif self.__count == 10:
                if self.__placement(
                        self.__p2_board,
                        row,
                        column,
                        orientation,
                        'P') == 0:
                    return -1

                print("Your opponent has placed their Patrol boats.")
                self.__count += 1

                self.__boardSetup = 0
                self.__turn = 1
                print("Your opponent is done placing ships!\nThe game will start now.")
                return 0

    def __placement(self, board, row, column, orientation, ship):
        # places the ships based on inputs from the self.__shipsplace()
        # function
        number = None
        placing = None

        if ship == 'C':
            placing = 5
            number = 1

        elif ship == 'B':
            placing = 4
            number = 2

        elif ship == 'D':
            placing = 3
            number = 3

        elif ship == 'S':
            placing = 3
            number = 4

        elif ship == 'P':
            placing = 2
            number = 5

        if orientation == 'v':
            for i in range(row, row + placing, 1):
                if row + placing > 10:
                    return 0  # returns 0 if the ships are going to be placed outside the board

                if board[i][column] != 0:
                    return 0  # returns 0 if the ships are going to overlap existing ships

            for i in range(row, row + placing, 1):
                board[i][column] = number
            return 1

        elif orientation == 'h':
            for i in range(column, column + placing, 1):
                if column + placing > 10:
                    return 0

                if board[row][i] != 0:
                    return 0

            for i in range(column, column + placing, 1):
                board[row][i] = number
            return 1

    def __attack(self, row, column):
        # checks if the user input is a hit or not and gives the user another
        # turn if it is
        if self.__usr == 1 and self.__turn == 1:

            if self.__p2_play[row][column] == 6 or self.__p2_play[row][column] == 7:
                print("You have already hit this one, please try again.")
                self.display(self.__p2_play)
                return -1

            elif 1 <= self.__p2_board[row][column] <= 5:
                print("You have hit a ship!")
                self.__p2_play[row][column] = 6
                shipsdownval = self.__shipsdown(
                    self.__p2_board, self.__p2_play)
                self.display(self.__p2_play)
                self.__displaydown(shipsdownval)
                if self.__checkwin() != -1:
                    print("\nYou go again.")
                return -1

            elif self.__p2_board[row][column] == 0:
                print("You missed..")
                self.__p2_play[row][column] = 7
                self.__turn = 2
                self.display(self.__p2_play)
                return 0

        if self.__usr == 1 and self.__turn == 2:

            if self.__p1_play[row][column] == 6 or self.__p1_play[row][column] == 7:
                return -1

            elif 1 <= self.__p1_board[row][column] <= 5:
                print(
                    "Your opponent has hit a ship at {}, {}..".format(
                        row + 1, column + 1))
                self.__p1_play[row][column] = 6
                shipsdownval = self.__shipsdown(
                    self.__p1_board, self.__p1_play)
                self.display(self.__p1_play)
                self.__displaydown(shipsdownval)
                if self.__checkwin() != -1:
                    print("\nYour opponent goes again.")
                return -1

            elif self.__p1_board[row][column] == 0:
                print("Your opponent missed!")
                self.__p1_play[row][column] = 7
                self.__turn = 1
                self.display(self.__p1_play)
                return 0

        if self.__usr == 2 and self.__turn == 1:

            if self.__p2_play[row][column] == 6 or self.__p2_play[row][column] == 7:
                return -1

            elif 1 <= self.__p2_board[row][column] <= 5:
                print(
                    "Your opponent has hit a ship at {}, {}..".format(
                        row + 1, column + 1))
                self.__p2_play[row][column] = 6
                shipsdownval = self.__shipsdown(
                    self.__p2_board, self.__p2_play)
                self.display(self.__p2_play)
                self.__displaydown(shipsdownval)
                if self.__checkwin() != -1:
                    print("\nYour opponent goes again.")
                return -1

            elif self.__p2_board[row][column] == 0:
                print("Your opponent missed!")
                self.__p2_play[row][column] = 7
                self.__turn = 2
                self.display(self.__p2_play)
                return 0

        elif self.__usr == 2 and self.__turn == 2:

            if self.__p1_play[row][column] == 6 or self.__p1_play[row][column] == 7:
                print("You have already hit this one, please try again.")
                return -1

            elif 1 <= self.__p1_board[row][column] <= 5:
                print("You have hit a ship!")
                self.__p1_play[row][column] = 6
                shipsdownval = self.__shipsdown(
                    self.__p1_board, self.__p1_play)
                self.display(self.__p1_play)
                self.__displaydown(shipsdownval)
                if self.__checkwin() != -1:
                    print("\nYou go again.")
                return -1

            elif self.__p1_board[row][column] == 0:
                print("You missed..")
                self.__p1_play[row][column] = 7
                self.__turn = 1
                self.display(self.__p1_play)
                return 0

    def __checkwin(self, userInput=None):  # checks to see if all ships have been struck
        # checks if 17 ships have been hit for either player or if the game has
        # been forfeited
        sum1 = 0
        sum2 = 0

        for i in range(10):
            for j in range(10):
                if self.__p1_play[i][j] == 6:
                    sum1 += 1
                if self.__p2_play[i][j] == 6:
                    sum2 += 1

        if sum1 == 17:
            if self.__firstWin == 0:
                print("Player 2 wins!")
            self.__firstWin = 1
            return -1

        if sum2 == 17:
            if self.__firstWin == 0:
                print("Player 1 wins!")
            self.__firstWin = 1
            return -1

        elif userInput == 'r':
            print("The game has been forfeited.")
            return -1

    def __shipsdown(self, board, play):
        # used to check if groups of ships are down
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0

        for i in range(10):
            for j in range(10):
                if play[i][j] == 6:
                    if board[i][j] == 1:
                        sum1 += 1
                    elif board[i][j] == 2:
                        sum2 += 1
                    elif board[i][j] == 3:
                        sum3 += 1
                    elif board[i][j] == 4:
                        sum4 += 1
                    elif board[i][j] == 5:
                        sum5 += 1

        if sum1 == 5:
            if(self.__u1ret1 == 0):
                self.__u1ret1 = 1
                return 1
            elif(self.__u2ret1 == 0):
                self.__u2ret1 = 1
                return 1

        if sum2 == 5:
            if(self.__u1ret2 == 0):
                self.__u1ret2 = 1
                return 1
            elif(self.__u2ret2 == 0):
                self.__u2ret2 = 1
                return 2

        if sum3 == 5:
            if(self.__u1ret3 == 0):
                self.__u1ret3 = 1
                return 3
            elif(self.__u2ret3 == 0):
                self.__u2ret3 = 1
                return 3

        if sum4 == 5:
            if(self.__u1ret4 == 0):
                self.__u1ret4 = 1
                return 4
            elif(self.__u2ret4 == 0):
                self.__u2ret4 = 1
                return 4

        if sum5 == 5:
            if(self.__u1ret5 == 0):
                self.__u1ret5 = 1
                return 5
            elif(self.__u2ret5 == 0):
                self.__u2ret5 = 1
                return 5

        else:
            return 0

    def __displaydown(self, element):
        # displays which ships are down based off inputs from
        # self.__shipsdown()
        if element == 1:
            print("\nCarrier ships down.")

        elif element == 2:
            print("\nBattleships down.")

        elif element == 3:
            print("\nDestroyer ships down.")

        elif element == 4:
            print("\nSubmarines down.")

        elif element == 5:
            print("\nPatrol boats down.")

        return

    def inputToGame(self, userInput):
        # facilitates the games main code and is used to control the games
        # various states
        orientation = None

        if self.__checkwin(userInput) == -1:
            return -1

        tempInput = userInput.split(',')

        try:
            row = int(tempInput[0])
            column = int(tempInput[1])
            if self.__boardSetup != 0:
                orientation = str(tempInput[2]).strip().lower()

        except (ValueError, IndexError):
            if (self.__usr == self.__turn or self.__usr == self.__boardSetup):
                print("Please enter in the format \"row, column(, orientation)\"..")
            return 0

        if row < 1 or row > 10:
            if (self.__usr == self.__turn or self.__usr == self.__boardSetup):
                print("Please enter a row between 1 and 10..")
            return 0

        elif column < 1 or column > 10:
            if (self.__usr == self.__turn or self.__usr == self.__boardSetup):
                print("Please enter a column between 1 and 10..")
            return 0

        if self.__boardSetup != 0:
            if orientation != 'h' and orientation != 'v':
                if (self.__usr == self.__turn or self.__usr == self.__boardSetup):
                    print("Please enter a valid orientation..")
                return 0

        row -= 1
        column -= 1

        if self.__boardSetup != 0:
            if self.__shipsplace(row, column, orientation) == -1:
                return 0

        elif self.__attack(row, column) == -1:
            if self.__checkwin() == -1:
                return -1
            return 0
        else:
            if self.__checkwin() == -1:
                return -1
            return 1
