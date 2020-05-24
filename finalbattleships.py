from network import *
from requests import get  # used to get your public IP address
from time import sleep
import copy
import sys
import time
import os
import shutil

network = Network_sockets()


class battleships:
    __firstRun = True
    __returner = False  # used to return -1 once the game is done executing

    __turn1 = True  # checks if its user 1's turn or not
    __turn2 = False

    # initializes the "boards" with value '0'
    __p1_board = [[0] * 10 for x in range(10)]
    __p2_board = [[0] * 10 for x in range(10)]
    __p1_play = [[0] * 10 for x in range(10)]
    __p2_play = [[0] * 10 for x in range(10)]
    __usr = None
    __p1_name = None
    __p2_name = None

    __ret1 = 0
    __ret2 = 0
    __ret3 = 0
    __ret4 = 0
    __ret5 = 0

    def __init__(self):
        self.intro()

    def intro(self):
        # gets width of terminal windows to center align text
        width = (shutil.get_terminal_size())[0]
        self.__clear()

        print("Welcome".center(width))  # center aligns text
        sleep(1)
        print("\n\n")
        print("to".center(width))
        sleep(1)
        print("\n\n")
        print("BATTLESHIPS".center(width))
        print("\n\n")
        sleep(1)

        while(1):
            self.__usr = str(
                input("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: "))
            if(self.__usr == '1'):
                # receives the public IP address from a handy online API
                ip = get("https://api.ipify.org").text
                print("Your public IP address is: ", ip)
                sleep(1)
                self.__typewriter("Waiting for a connection.. ")
                network.host()
                break

            elif(self.__usr == '2'):
                network.connect()
                break

            elif (self.__usr == '3'):
                self.__returner = True
                return

            else:
                print("Please enter one of the above options..")
                sleep(3)
                self.__clear()

        if(self.__usr == '1'):
            # asks user to enter name (on the host's and receiver's end)
            self.__p1_name = str(input("Enter your name: "))
            sleep(0.1)
            # sends the user's name to opponent's program
            network.send(self.__p1_name)
            # receives the user name from the opponent's program
            self.__p2_name = network.receive()
            self.__clear()
            print("Hello " + self.__p1_name + ".\nTime to place your ships!")
            sleep(3)

            self.__shipsplace(self.__p1_board)
            self.__display(self.__p1_board)

            try:
                if(int(network.receive())):
                    input("Press ENTER to continue ")

                else:
                    print("\nWaiting for " + self.__p2_name + "..")
                    # ensures that the host program doesn't keep going while
                    # the opponent is not done
                    if(int(network.receive())):
                        print("\nOk, we're done waiting.")
                        input("Press ENTER to continue ")

            except ValueError:
                input("Press ENTER to continue ")

        elif(self.__usr == '2'):
            self.__p2_name = str(input("Enter your name: "))
            self.__p1_name = network.receive()
            sleep(0.1)
            network.send(self.__p2_name)
            sleep(0.1)
            network.send(0)
            self.__clear()
            print("Hello " + self.__p2_name + ".\nTime to place your ships")
            sleep(3)

            self.__shipsplace(self.__p2_board)
            self.__display(self.__p2_board)
            input("\nPress ENTER to continue ")
            sleep(0.1)
            network.send(1)

    def __clear(self):

        if os.name == "nt":  # defines the clear function for Windows machines
            os.system("cls")

        else:  # defines the clear function for Linux-based machines
            os.system("clear")

        return

    def __typewriter(self, message):

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)

        return

    def __conversion(self, board, row, column):
        # since the program uses numbers, this function converts the numbers to
        # make sense to the user
        if(board[row][column] == 0):
            return str(' ')

        elif(board[row][column] == 1):
            return str('C')

        elif(board[row][column] == 2):
            return str('B')

        elif(board[row][column] == 3):
            return str('D')

        elif(board[row][column] == 4):
            return str('S')

        elif(board[row][column] == 5):
            return str('P')

        elif(board[row][column] == 6):
            return str('$')

        elif(board[row][column] == 7):
            return str('*')

    def __display(self, board):

        row = 0  # represents each rows
        # prints the line numbers horizontally
        print("\n     1   2   3   4   5   6   7   8   9   10")

        for i in range(21):
            if (i % 2 == 0):
                print("   +---+---+---+---+---+---+---+---+---+---+",
                      end='\n')  # prints the border for the grid

            else:  # prints the line number vertically with appropriate spacing
                if((i // 2) + 1) != 10:
                    print(str((i // 2) + 1), end="  ")

                else:
                    print(str((i // 2) + 1), end=' ')

                column = 0  # represents each element horizontally
                for j in range(10):
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

    def __shipsplace(self, board):

        while(1):
            self.__clear()
            row = 0
            column = 0
            self.__display(board)
            print("Placing Carrier ships now")

            try:
                # takes the row number from the user
                row = int(input("Enter the row: "))

            except ValueError:
                # prevents the program from crashing when a non-integer is
                # entered
                print("Please enter a number..\n")
                sleep(2)  # insert
                continue  # loops the enclosed portion of code when user error occurs to take inputs again

            if(row < 1 or row > 10):  # ensures the input is between 1 and 10
                print("Please enter a row between 1 and 10..")
                # adds a pause to allow the user to read the error before
                # disappearing rudely
                sleep(2)
                continue

            try:
                # takes the column number from the user
                column = int(input("Enter the column: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(column < 1 or column > 10):
                print("Please enter a column between 1 and 10..")
                sleep(2)
                continue

            # takes the orientation of ships to be placeed from user
            orientation = input(
                "Enter the orientation (v for vertical, h for horizontal): ").lower()
            if(orientation != 'h' and orientation != 'v'):  # raises error neither h or v are entered
                print("Please enter either v or h..")
                sleep(2)
                continue

            # checks to see if the rows/columns aren't already occupied
            if(self.__placement(board, row - 1, column - 1, orientation, 'C') == 0):
                print(
                    "\nThe ships could not be placed..\nPlease check the board and try again.")
                input("Press ENTER to continue ")
                continue

            break

        self.__clear()
        print("The ships have been placed.")
        sleep(1)

        while(1):
            self.__clear()
            row = 0
            column = 0
            self.__display(board)
            print("Placing Battleships now")

            try:
                row = int(input("Enter the row: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(row < 1 or row > 10):
                print("Please enter a row between 1 and 10..")
                sleep(2)
                continue

            try:
                column = int(input("Enter the column: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(column < 1 or column > 10):
                print("Please enter a column between 1 and 10..")
                sleep(2)
                continue

            orientation = input(
                "Enter the orientation (v for vertical, h for horizontal): ").lower()
            if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

            if(self.__placement(board, row - 1, column - 1, orientation, 'B') == 0):
                print(
                    "\nThe ships could not be placed..\nPlease check the board and try again.")
                input("Press ENTER to continue ")
                continue

            break

        self.__clear()
        print("The ships have been placed.")
        sleep(1)

        while(1):
            self.__clear()
            row = 0
            column = 0
            self.__display(board)
            print("Placing Destroyer ships now")

            try:
                row = int(input("Enter the row: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(row < 1 or row > 10):
                print("Please enter a row between 1 and 10..")
                sleep(2)
                continue

            try:
                column = int(input("Enter the column: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(column < 1 or column > 10):
                print("Please enter a column between 1 and 10..")
                sleep(2)
                continue

            orientation = input(
                "Enter the orientation (v for vertical, h for horizontal): ").lower()
            if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

            if(self.__placement(board, row - 1, column - 1, orientation, 'D') == 0):
                print(
                    "\nThe ships could not be placed..\nPlease check the board and try again.")
                input("Press ENTER to continue ")
                continue

            break

        self.__clear()
        print("The ships have been placed.")
        sleep(1)

        while(1):
            self.__clear()
            row = 0
            column = 0
            self.__display(board)
            print("Placing Submarines now")

            try:
                row = int(input("Enter the row: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(row < 1 or row > 10):
                print("Please enter a row between 1 and 10..")
                sleep(2)
                continue

            try:
                column = int(input("Enter the column: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(column < 1 or column > 10):
                print("Please enter a column between 1 and 10..")
                sleep(2)
                continue

            orientation = input(
                "Enter the orientation (v for vertical, h for horizontal): ").lower()
            if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

            if(self.__placement(board, row - 1, column - 1, orientation, 'S') == 0):
                print(
                    "\nThe ships could not be placed..\nPlease check the board and try again.")
                input("Press ENTER to continue ")
                continue

            break

        self.__clear()
        print("The ships have been placed.")
        sleep(1)

        while(1):
            self.__clear()
            row = 0
            column = 0
            self.__display(board)
            print("Placing Patrol boats now")

            try:
                row = int(input("Enter the row: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(row < 1 or row > 10):
                print("Please enter a row between 1 and 10..")
                sleep(2)
                continue

            try:
                column = int(input("Enter the column: "))

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            if(column < 1 or column > 10):
                print("Please enter a column between 1 and 10..")
                sleep(2)
                continue

            orientation = input(
                "Enter the orientation (v for vertical, h for horizontal): ").lower()
            if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

            if(self.__placement(board, row - 1, column - 1, orientation, 'P') == 0):
                print(
                    "\nThe ships could not be placed..\nPlease check the board and try again.")
                input("Press ENTER to continue ")
                continue

            break

        self.__clear()
        print("The ships have been placed.")
        sleep(1)

        return

    # places the ships based on inputs from the self.__shipsplace() function
    def __placement(self, board, row, column, orientation, ship):

        if(ship == 'C'):
            placing = 5
            number = 1

        elif(ship == 'B'):
            placing = 4
            number = 2

        elif(ship == 'D'):
            placing = 3
            number = 3

        elif(ship == 'S'):
            placing = 3
            number = 4

        elif(ship == 'P'):
            placing = 2
            number = 5

        if(orientation == 'v'):
            for i in range(row, row + placing, 1):
                if(row + placing > 10):
                    return 0  # returns 0 if the ships are going to be placed outside the board

                if(board[i][column] != 0):
                    return 0  # returns 0 if the ships are going to overlap existing ships

            for i in range(row, row + placing, 1):
                board[i][column] = number
            return 1

        elif(orientation == 'h'):
            for i in range(column, column + placing, 1):
                if(column + placing > 10):
                    return 0

                if(board[row][i] != 0):
                    return 0

            for i in range(column, column + placing, 1):
                board[row][i] = number
            return 1

    def __attack(self, play):  # takes input from the user and evaluates it against the opponent's board

        while(1):
            self.__display(play)
            try:
                row = int(input("Enter the row: "))
                if(row < 1 or row > 10):
                    print("Please enter a row between 1 and 10..\n")
                    sleep(2)
                    continue
                row -= 1  # computers count from 0, so 1 is subtracted from the input

            except ValueError:
                print("Please enter a number..\n")
                continue

            try:
                column = int(input("Enter the column: "))
                if(column < 1 or column > 10):
                    print("Please enter a column between 1 and 10..\n")
                    sleep(2)
                    continue
                column -= 1

            except ValueError:
                print("Please enter a number..\n")
                sleep(2)
                continue

            sleep(0.1)  # improves reliability while sending
            # sends the row and column to the opponent's program to evaluate
            # the changes
            network.send(row)
            sleep(0.1)
            network.send(column)

            print("\nSent.")
            print("Waiting for an input..\n")

            try:
                # receives an input from the opponent's program and performs
                # the relevant actions according to the input received
                element = int(network.receive())
                if(element == 4):
                    # occurs when the opponent's program is not ready to
                    # receive the input but has already been sent by the host
                    # program
                    print("Data was lost in transmission, please try again.")
                    sleep(2)
                    self.__clear()
                    continue

            except ValueError:
                print("Data was lost in transmission, please try again.")
                sleep(2)
                self.__clear()
                continue

            if(element == 1):
                print("You have already hit this one, please try again.")
                sleep(2)
                self.__clear()
                continue

            elif(element == 2):
                play[row][column] = 6
                print("Nice, you have sunk a ship!\nYour move again.")
                self.__displaydown(int(network.receive()))
                sleep(1)
                sleep(0.1)

                if(self.__checkwin(play)):  # sends a unique string if the user has won
                    sleep(0.1)
                    network.send("Win")
                    break

                else:
                    sleep(0.1)
                    network.send("No")

                network.send(1)
                continue

            elif(element == 3):
                play[row][column] = 7
                print("You missed.")
                sleep(0.1)
                network.send("No")

            sleep(0.1)
            network.send(0)

            break

        return

    # evaluates the opponent's inputs against the player's board
    def __evaluate(self, play, board, name):

        while(1):
            try:  # receives the inputs from the self.__attack() function
                row = int(network.receive())
                column = int(network.receive())
                if not (
                    (row >= 0 and row <= 9) or (
                        column >= 0 and column <= 9)):
                    sleep(0.1)
                    network.send(4)
                    continue
            except ValueError:
                sleep(0.1)
                # loops the program and starts listening again if the program
                # receives garbled inputs from the opponent's program and asks
                # it to loop its function
                network.send(4)
                continue

            if(play[row][column] == 6 or play[row][column] == 7):
                sleep(0.1)
                network.send(1)
                continue

            elif(board[row][column] >= 1 and board[row][column] <= 5):
                print(name + " has hit your ship..")
                play[row][column] = 6
                sleep(0.1)
                network.send(2)
                shipsdownval = self.__shipsdown(board, play)
                sleep(0.1)
                network.send(shipsdownval)
                self.__displaydown(shipsdownval)

            elif(board[row][column] == 0):
                print(name + " missed.")
                play[row][column] = 7
                sleep(0.1)
                network.send(3)

            # checks if unique string has been received, in which case the loop
            # is broken
            if(network.receive() == "Win"):
                break

            try:
                save = network.receive()
                if(int(save)):
                    print("\n" + name + " goes again.")
                    continue
            except ValueError:
                if(save == "No"):
                    continue
                if(int(network.receive())):
                    print("\n" + name + " goes again.")
                    continue

            break

        return

    def __checkwin(self, play):  # checks to see if all ships have been struck

        sum = 0

        for i in range(10):
            for j in range(10):
                if(play[i][j] == 6):
                    sum += 1

        if(sum == 17):
            return 1

        return 0

    def __shipsdown(self, board, play):

        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0

        for i in range(10):
            for j in range(10):
                if(play[i][j] == 6):
                    if(board[i][j] == 1):
                        sum1 += 1
                    elif(board[i][j] == 2):
                        sum2 += 1
                    elif(board[i][j] == 3):
                        sum3 += 1
                    elif(board[i][j] == 4):
                        sum4 += 1
                    elif(board[i][j] == 5):
                        sum5 += 1

        if(sum1 == 5 and self.__ret1 == 0):
            self.__ret1 = 1
            return 1

        if(sum2 == 4 and self.__ret2 == 0):
            self.__ret2 = 1
            return 2

        if(sum3 == 3 and self.__ret3 == 0):
            self.__ret3 = 1
            return 3

        if(sum4 == 3 and self.__ret4 == 0):
            self.__ret4 = 1
            return 4

        if(sum5 == 2 and self.__ret5 == 0):
            self.__ret5 = 1
            return 5

        else:
            return 0

    def __displaydown(self, element):

        if(element == 1):
            print("\nCarrier ships down.")
            sleep(1)

        elif(element == 2):
            print("\nBattleships down.")
            sleep(1)

        elif(element == 3):
            print("\nDestroyer ships down.")
            sleep(1)

        elif(element == 4):
            print("\nSubmarines down.")
            sleep(1)

        elif(element == 5):
            print("\nPatrol boats down.")
            sleep(1)

        return

    def game(self):

        if(self.__returner):
            return -1

        if(self.__usr == '1'):
            if(self.__firstRun):
                self.__firstRun = not self.__firstRun
                return 0

            while(1):
                if(self.__turn1):
                    self.__clear()
                    print("Time to strike!")
                    self.__attack(self.__p1_play)
                    self.__display(self.__p1_play)
                    if(self.__checkwin(self.__p1_play)):  # sends a unique string if the user has won
                        sleep(0.1)
                        network.send("Win")
                        break

                    else:
                        sleep(0.1)
                        network.send("No")

                    input("Press ENTER to continue ")
                    self.__turn1 = not self.__turn1
                    return 1

                else:
                    self.__clear()
                    print(self.__p2_name + " moves..")
                    self.__evaluate(
                        self.__p2_play, self.__p1_board, self.__p2_name)
                    self.__display(self.__p2_play)
                    # checks if unique string has been received, in which case
                    # the loop is broken
                    if(network.receive() == "Win"):
                        break

                    input("Press ENTER to continue ")
                    self.__clear()
                    self.__turn1 = not self.__turn1
                    return 0

        elif(self.__usr == '2'):
            if(self.__firstRun):
                self.__firstRun = not self.__firstRun
                return 1

            while(1):
                if(self.__turn2):
                    print("Time to strike!")
                    self.__attack(self.__p2_play)
                    self.__display(self.__p2_play)
                    if(self.__checkwin(self.__p2_play)):
                        sleep(0.1)
                        network.send("Win")
                        break

                    else:
                        sleep(0.1)
                        network.send("No")

                    input("Press ENTER to continue ")
                    self.__turn2 = not self.__turn2
                    return 1
                else:
                    self.__clear()
                    print(self.__p1_name + " moves..")
                    self.__evaluate(
                        self.__p1_play, self.__p2_board, self.__p1_name)
                    self.__display(self.__p1_play)
                    if(network.receive() == "Win"):
                        break

                    input("Press ENTER to continue ")
                    self.__clear()
                    self.__turn2 = not self.__turn2
                    return 0

        if(self.__checkwin(self.__p1_play)):  # checks to see which player has one
            self.__clear()
            self.__typewriter(self.__p1_name + " wins!")
            sleep(5)
            self.__clear()

        else:
            self.__clear()
            self.__typewriter(self.__p2_name + " wins!")
            sleep(5)
            self.__clear()

        network.close()
        self.intro()


Battleships = battleships()
while(1):
    if(Battleships.game() == -1):
        break