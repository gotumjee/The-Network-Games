from network import *
from requests import get
#from colorama import Fore
from time import sleep
import copy, sys, time, os, shutil

network = Network_sockets()

def clear(): 
  
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def conversion(board, row, column):
    if(board[row][column]==0):
        return str(' ')
    elif(board[row][column]==1):
        return str('C')
    elif(board[row][column]==2):
        return str('B')
    elif(board[row][column]==3):
        return str('D')
    elif(board[row][column]==4):
        return str('S')
    elif(board[row][column]==5):
        return str('P')
    elif(board[row][column]==6):
        return str('$')
    elif(board[row][column]==7):
        return str('*')

    return

def display(board):
    row = 0
    print("\n     1   2   3   4   5   6   7   8   9   10")
    for i in range(21):
        if (i%2==0):
            print("   +---+---+---+---+---+---+---+---+---+---+", end='\n')
        else:
            if((i//2)+1)!=10:
                print(str((i//2)+1), end="  ")
            else:
                print(str((i//2)+1), end=" ")
            column = 0
            for j in range(10):
                print("| " + conversion(board, row, column), end=' ')
                column += 1
            print('|', end='')
            row += 1
            print("\n", end='')

    return

def shipsplace(board):
    while(1):
        clear()
        row = 0
        column = 0
        display(board)
        print("Placing Carrier ships now")
        try:
            row = int(input("Enter the row: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(row<1 or row>10):
            print("Please enter a row between 1 and 10..")
            sleep(2)
            continue
        try:
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(column<1 or column>10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue
        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation!='h' and orientation!='v'):
                print("Please enter either v or h..")
                sleep(2)
                continue
        if(placement(board, row-1, column-1, orientation, 'C')==0):
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
        if(row<1 or row>10):
            print("Please enter a row between 1 and 10..")
            sleep(2)
            continue
        try:
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(column<1 or column>10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue
        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation!='h' and orientation!='v'):
                print("Please enter either v or h..")
                sleep(2)
                continue
        if(placement(board, row-1, column-1, orientation, 'B')==0):
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
        if(row<1 or row>10):
            print("Please enter a row between 1 and 10..")
            sleep(2)
            continue
        try:
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(column<1 or column>10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue
        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation!='h' and orientation!='v'):
                print("Please enter either v or h..")
                sleep(2)
                continue
        if(placement(board, row-1, column-1, orientation, 'D')==0):
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
        print("Placing Submarine ships now")
        try:
            row = int(input("Enter the row: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(row<1 or row>10):
            print("Please enter a row between 1 and 10..")
            sleep(2)
            continue
        try:
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(column<1 or column>10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue
        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation!='h' and orientation!='v'):
                print("Please enter either v or h..")
                sleep(2)
                continue
        if(placement(board, row-1, column-1, orientation, 'S')==0):
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
        if(row<1 or row>10):
            print("Please enter a row between 1 and 10..")
            sleep(2)
            continue
        try:
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        if(column<1 or column>10):
            print("Please enter a column between 1 and 10..")
            sleep(2)
            continue
        orientation = input("Enter the orientation (v for vertical, h for horizontal): ").lower()
        if(orientation!='h' and orientation!='v'):
                print("Please enter either v or h..")
                sleep(2)
                continue
        if(placement(board, row-1, column-1, orientation, 'P')==0):
            print("\nThe ships could not be placed..\nPlease check the board and try again.")
            input("Press ENTER to continue ")
            continue
        break
    clear()
    print("The ships have been placed.")
    sleep(1)

    return

def placement(board, row, column, orientation, ship):
    if(ship=='C'):
        placing=5
        number=1
    elif(ship=='B'):
        placing=4
        number=2
    elif(ship=='D'):
        placing=3
        number=3
    elif(ship=='S'):
        placing=3
        number=4
    elif(ship=='P'):
        placing=2
        number=5
    if(orientation=='v'):
        for i in range(row, row+placing, 1):
            if(row+placing>10):
                return 0
            if(board[i][column]!=0):
                return 0
        for i in range(row, row+placing, 1):
            board[i][column]=number
        return 1
    if(orientation=='h'):
        for i in range(column, column+placing, 1):
            if(column+placing>10):
                return 0
            if(board[row][i]!=0):
                return 0
        for i in range(column, column+placing, 1):
            board[row][i]=number
        return 1

def attack(play):
    
    while(1):

        display(play)
        try:
            row = int(input("Enter the row: "))
            if(row<1 or row>10):
                print("Please enter a row between 1 and 10..\n")
                sleep(2)
                continue
            row-=1
        except ValueError:
            print("Please enter a number..\n")
            continue   
        try:
            column = int(input("Enter the column: "))
            if(column<1 or column>10):
                print("Please enter a column between 1 and 10..\n")
                sleep(2)
                continue
            column-=1
        except ValueError:
            print("Please enter a number..\n")
            sleep(2)
            continue
        
        network.send(row)
        network.send(column)

        element = int(network.receive())
        if(element == 1):
            print("You have already hit this one, please try again.")
            sleep(1)
            clear()
            continue

        elif(element == 2):
            play[row][column] = 6
            print("Nice, you have sunk a ship!")

        elif(element == 3):
            play[row][column] = 7
            print("You missed.")

        break

    return
    
def evaluate(play, board, name):

    while(1):

        row = int(network.receive())
        column = int(network.receive())

        if(play[row][column] == 6 or play[row][column] == 7):
            network.send(1)
            continue
        elif(board[row][column]>=1 and board[row][column]<=5):
            print(name + " has hit your ship..")
            play[row][column] = 6
            network.send(2)
        elif(board[row][column]==0):
            print(name + " missed.")
            play[row][column] = 7
            network.send(3)
        
        break

    return

def checkwin(play):
    sum=0
    for i in range(10):
        for j in range(10):
            if(play[i][j]==6):
                sum+=1
    if(sum==17):
        return 1
    return 0
    
def main():
    width = (shutil.get_terminal_size())[0]
    clear()
    print("Welcome".center(width))
    sleep(1)
    print("\n\n")
    print("to".center(width))
    sleep(1)
    print("\n\n")
    print("🅑🅐🅣🅣🅛🅔🅢🅗🅘🅟🅢".center(width))
    print("\n\n")
    sleep(1)
    while(1):
        while(1):
            usr = str(input("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: "))
            if(usr == '1'):
                ip = get("https://api.ipify.org").text
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

        p1_board = [[0]*10 for x in range(10)]
        p2_board = [[0]*10 for x in range(10)]
        p1_play = [[0]*10 for x in range(10)]
        p2_play = [[0]*10 for x in range(10)]

        if(usr == '1'):
            p1_name = str(input("Enter your name: "))
            network.send(p1_name)
            p2_name = network.receive()
            clear()
            print("Hello " + p1_name +".\nTime to place your ships!")
            sleep(2)
            shipsplace(p1_board)
            display(p1_board)
            try:
                if(int(network.receive())):
                    input("Press ENTER to continue ")
                else:
                    print("\nWaiting for " + p2_name + "..")
                    if(int(network.receive())):
                        print("\nOk, we're done waiting.")
                        input("Press ENTER to continue ")
            except ValueError:
                input("Press ENTER to continue ")
        
        elif(usr == '2'):
            p2_name = str(input("Enter your name: "))
            p1_name = network.receive()
            network.send(p2_name)
            network.send(0)
            clear()
            print("Hello " + p2_name +".\nTime to place your ships")
            sleep(2)
            shipsplace(p2_board)
            display(p2_board)
            input("\nPress ENTER to continue ")
            network.send(1)

        if(usr == '1'):
            while(1):
                clear()
                print("Time to strike!")
                attack(p1_play)
                display(p1_play)
                if(checkwin(p1_play)):
                    network.send("Win")
                    break
                else:
                    network.send("No")
                input("Press ENTER to continue ")
                clear()
                print(p2_name + " moves..")
                evaluate(p2_play, p1_board, p2_name)
                display(p2_play)
                if(network.receive()=="Win"):
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
                    network.send("Win")
                    break
                else:
                    network.send("No")
                input("Press ENTER to continue ")

        if(checkwin(p1_play)):
            typewriter(p1_name + " wins!")
            sleep(3)
            continue
        else:
            typewriter(p2_name + " wins!")
            sleep(3)
            continue

        network.close()

if __name__ == "__main__":
    main()