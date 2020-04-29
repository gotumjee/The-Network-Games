from network import *
from requests import get #used to get your public IP address
#from colorama import Fore
from time import sleep
import copy, sys, time, os, shutil

network = Network_sockets()

class downships:
    ret1 = 0
    ret2 = 0
    ret3 = 0
    ret4 = 0
    ret5 = 0

def clear():

    if os.name == "nt": #defines the clear function for Windows machines
        os.system("cls")

    else: #defines the clear function for Linux-based machines
        os.system("clear")

    return

def typewriter(message):

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    return

def conversion(board, row, column):
    #since the program uses numbers, this function converts the numbers to make sense to the user
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

def display(board):

    row = 0 #represents each rows
    print("\n     1   2   3   4   5   6   7   8   9   10") #prints the line numbers horizontally

    for i in range(21):
        if (i%2 == 0):
            print("   +---+---+---+---+---+---+---+---+---+---+", end = '\n') #prints the border for the grid

        else: #prints the line number vertically with appropriate spacing
            if((i//2)+1) != 10:
                print(str((i//2)+1), end = "  ")

            else:
                print(str((i//2)+1), end = ' ')

            column = 0 #represents each element horizontally
            for j in range(10):
                print("| " + conversion(board, row, column), end = ' ') #prints the ships to the screen (using the conversion() function) with appropriate borders and spacing
                column += 1 #increments column to move to the next element

            print('|')
            row += 1  #moves to the next row

    return

def shipsplace(board):

    while(1):
        clear()
        row = 0
        column = 0
        display(board)
        print("Placing Carrier ships now")

        try:
            row = int(input("Enter the row: ")) #takes the row number from the user

        except ValueError:
            print("Please enter a number..\n") #prevents the program from crashing when a non-integer is entered
            sleep(2) #insert
            continue #loops the enclosed portion of code when user error occurs to take inputs again

        if(row < 1 or row > 10): #ensures the input is between 1 and 10
            print("Please enter a row between 1 and 10..")
            sleep(2) #adds a pause to allow the user to read the error before disappearing rudely
            continue

        try:
            column = int(input("Enter the column: ")) #takes the column number from the user

        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue

        if(column < 1 or column > 10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue

        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower() #takes the orientation of ships to be placeed from user
        if(orientation != 'h' and orientation != 'v'): #raises error neither h or v are entered
                print("Please enter either v or h..")
                sleep(2)
                continue

        if(placement(board, row-1, column-1, orientation, 'C') == 0): #checks to see if the rows/columns aren't already occupied
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue

        break

    clear()
    print("The ships have been placed.")
    sleep(1)

    while(1):
        clear()
        row = 0
        column = 0
        display(board)
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

        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

        if(placement(board, row-1, column-1, orientation, 'B') == 0):
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue

        break

    clear()
    print("The ships have been placed.")
    sleep(1)

    while(1):
        clear()
        row = 0
        column = 0
        display(board)
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

        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

        if(placement(board, row-1, column-1, orientation, 'D') == 0):
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue

        break

    clear()
    print("The ships have been placed.")
    sleep(1)

    while(1):
        clear()
        row = 0
        column = 0
        display(board)
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

        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

        if(placement(board, row-1, column-1, orientation, 'S') == 0):
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue

        break

    clear()
    print("The ships have been placed.")
    sleep(1)

    while(1):
        clear()
        row = 0
        column = 0
        display(board)
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

        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation != 'h' and orientation != 'v'):
                print("Please enter either v or h..")
                sleep(2)
                continue

        if(placement(board, row-1, column-1, orientation, 'P') == 0):
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue

        break

    clear()
    print("The ships have been placed.")
    sleep(1)

    return

def placement(board, row, column, orientation, ship): #places the ships based on inputs from the shipsplace() function

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
        for i in range(row, row+placing, 1):
            if(row+placing > 10):
                return 0 #returns 0 if the ships are going to be placed outside the board

            if(board[i][column] != 0):
                return 0 #returns 0 if the ships are going to overlap existing ships

        for i in range(row, row+placing, 1):
            board[i][column] = number
        return 1

    elif(orientation == 'h'):
        for i in range(column, column+placing, 1):
            if(column+placing > 10):
                return 0

            if(board[row][i] != 0):
                return 0

        for i in range(column, column+placing, 1):
            board[row][i] = number
        return 1

def attack(play): #takes input from the user and evaluates it against the opponent's board

    while(1):
        display(play)
        try:
            row = int(input("Enter the row: "))
            if(row < 1 or row > 10):
                print("Please enter a row between 1 and 10..\n")
                sleep(2)
                continue
            row -= 1 #computers count from 0, so 1 is subtracted from the input

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

        sleep(0.1) #improves reliability while sending
        network.send(row) #sends the row and column to the opponent's program to evaluate the changes
        sleep(0.1)
        network.send(column)

        print("\nSent.")
        print("Waiting for an input..\n")

        try:
            element = int(network.receive()) #receives an input from the opponent's program and performs the relevant actions according to the input received
            if(element == 4):
                print("Data was lost in transmission, please try again.") #occurs when the opponent's program is not ready to receive the input but has already been sent by the host program
                sleep(2)
                clear()
                continue

        except ValueError:
            print("Data was lost in transmission, please try again.")
            sleep(2)
            clear()
            continue

        if(element == 1):
            print("You have already hit this one, please try again.")
            sleep(1)
            clear()
            continue

        elif(element == 2):
            play[row][column] = 6
            print("Nice, you have sunk a ship!\nYour move again.")
            displaydown(int(network.receive()))
            sleep(1)
            sleep(0.1)

            if(checkwin(play)): #sends a unique string if the user has won
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

def evaluate(play, board, name): #evaluates the opponent's inputs against the player's board

    while(1):
        try: #receives the inputs from the attack() function
            row = int(network.receive())
            column = int(network.receive())
            if not ((row >= 0 and row <= 9) or (column >= 0 and column <= 9)):
                sleep(0.1)
                network.send(4)
                continue
        except ValueError:
            sleep(0.1)
            network.send(4) #loops the program and starts listening again if the program receives garbled inputs from the opponent's program and asks it to loop its function
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
            shipsdownval = shipsdown(board, play)
            sleep(0.1)
            network.send(shipsdownval)
            displaydown(shipsdownval)

        elif(board[row][column] == 0):
            print(name + " missed.")
            play[row][column] = 7
            sleep(0.1)
            network.send(3)

        if(network.receive()=="Win"): #checks if unique string has been received, in which case the loop is broken
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

def checkwin(play): #checks to see if all ships have been struck

    sum = 0

    for i in range(10):
        for j in range(10):
            if(play[i][j] == 6):
                sum += 1

    if(sum == 17):
        return 1

    return 0

def shipsdown(board, play):
 
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    for i in range(10):
        for j in range(10):
            if(play[i][j] == 6):
                if(board[i][j] == 1):
                    sum1+=1
                elif(board[i][j] == 2):
                    sum2+=1
                elif(board[i][j] == 3):
                    sum3+=1
                elif(board[i][j] == 4):
                    sum4+=1
                elif(board[i][j] == 5):
                    sum5+=1
    
    if(sum1 == 5 and downships.ret1 == 0):
        downships.ret1 = 1
        return 1

    if(sum2 == 4 and downships.ret2 == 0):
        downships.ret2=1
        return 2

    if(sum3 == 3 and downships.ret3 == 0):
        downships.ret3=1
        return 3

    if(sum4 == 3 and downships.ret4 == 0):
        downships.ret4=1
        return 4

    if(sum5 == 2 and downships.ret5 == 0):
        downships.ret5=1
        return 5

    else:
        return 0

def displaydown(element):

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

def main():
    width = (shutil.get_terminal_size())[0] #gets width of terminal windows to center align text
    clear()

    print("Welcome".center(width)) #center aligns text
    sleep(1)
    print("\n\n")
    print("to".center(width))
    sleep(1)
    print("\n\n")
    print("BATTLESHIPS".center(width))
    print("\n\n")

    sleep(1)
    while(1):
        while(1):
            usr = str(input("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: "))
            if(usr == '1'):
                ip = get("https://api.ipify.org").text #receives the public IP address from a handy online API
                print("Your public IP address is: ", ip)
                sleep(1)
                typewriter("Waiting for a connection..")
                network.host()
                break

            elif(usr == '2'):
                network.connect()
                break

            elif (usr == '3'):
                sys.exit()

            else:
                print("Please enter one of the above options..")
                sleep(3)
                clear()
                continue


        p1_board = [[0]*10 for x in range(10)] #initializes the "boards" with value '0'
        p2_board = [[0]*10 for x in range(10)]
        p1_play = [[0]*10 for x in range(10)]
        p2_play = [[0]*10 for x in range(10)]

        if(usr == '1'):
            p1_name = str(input("Enter your name: ")) #asks user to enter name (on the host's and receiver's end)
            sleep(0.1)
            network.send(p1_name) #sends the user's name to opponent's program
            p2_name = network.receive() #receives the user name from the opponent's program
            clear()
            print("Hello " + p1_name +".\nTime to place your ships!")
            sleep(3)
            shipsplace(p1_board)
            display(p1_board)
            try:
                if(int(network.receive())):
                    input("Press ENTER to continue ")

                else:
                    print("\nWaiting for " + p2_name + "..")
                    if(int(network.receive())): #ensures that the host program doesn't keep going while the opponent is not done
                        print("\nOk, we're done waiting.")
                        input("Press ENTER to continue ")

            except ValueError:
                input("Press ENTER to continue ")

        elif(usr == '2'):
            p2_name = str(input("Enter your name: "))
            p1_name = network.receive()
            sleep(0.1)
            network.send(p2_name)
            sleep(0.1)
            network.send(0)
            clear()
            print("Hello " + p2_name +".\nTime to place your ships")
            sleep(3)
            shipsplace(p2_board)
            display(p2_board)
            input("\nPress ENTER to continue ")
            sleep(0.1)
            network.send(1)

        if(usr == '1'):
            while(1):
                clear()
                print("Time to strike!")
                attack(p1_play)
                display(p1_play)
                if(checkwin(p1_play)): #sends a unique string if the user has won
                    sleep(0.1)
                    network.send("Win")
                    break

                else:
                    sleep(0.1)
                    network.send("No")

                input("Press ENTER to continue ")
                clear()
                print(p2_name + " moves..")
                evaluate(p2_play, p1_board, p2_name)
                display(p2_play)
                if(network.receive()=="Win"): #checks if unique string has been received, in which case the loop is broken
                    break

                input("Press ENTER to continue ")

        elif(usr == '2'):
            while(1):
                clear()
                print(p1_name + " moves..")
                evaluate(p1_play, p2_board, p1_name)
                display(p1_play)
                if(network.receive()=="Win"):
                    break

                input("Press ENTER to continue ")
                clear()
                print("Time to strike!")
                attack(p2_play)
                display(p2_play)
                if(checkwin(p2_play)):
                    sleep(0.1)
                    network.send("Win")
                    break

                else:
                    sleep(0.1)
                    network.send("No")

                input("Press ENTER to continue ")

        if(checkwin(p1_play)): #checks to see which player has one
            clear()
            typewriter(p1_name + " wins!")
            sleep(5)
            clear()
            continue

        else:
            clear()
            typewriter(p2_name + " wins!")
            sleep(5)
            clear()
            continue

        network.close()

if __name__ == "__main__":
    main()