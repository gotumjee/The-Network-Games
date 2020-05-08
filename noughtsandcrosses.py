from network import *
from GridModule import *
import sys
from time import sleep

network = Network_sockets()
grid = Grid(3, 3, ' ')

#check if victory conditions have been met
#returns true or false
def check_win(grid, char):
    #check rows
    for i in range(3):
        if(grid.getCellValue(0,i)==char and grid.getCellValue(1,i)==char and grid.getCellValue(2,i)==char):
                return True
    #check columns
    for i in range(3):
        if(grid.getCellValue(i,0)==char and grid.getCellValue(i,1)==char and grid.getCellValue(i,2)==char):
                return True
    #check diagonals
    if(grid.getCellValue(0,0)==char and grid.getCellValue(1,1)==char and grid.getCellValue(2,2)==char):
        return True
    if(grid.getCellValue(0,2)==char and grid.getCellValue(1,1)==char and grid.getCellValue(2,0)==char):
        return True
    return False

#check if the board is full
def check_full(grid):
    #check every cell, if any are empty, return Flase
    for i in range(3):
        for a in range(3):
            if(grid.getCellValue(a,i)==' '):
                return False
    return True

#draw grid
def draw_grid(grid):
    print("\n\n%s|%s|%s\n-----\n%s|%s|%s\n-----\n%s|%s|%s\n" % (grid.getCellValue(0,0), grid.getCellValue(0,1), grid.getCellValue(0,2), grid.getCellValue(1,0), grid.getCellValue(1,1), grid.getCellValue(1,2), grid.getCellValue(2,0), grid.getCellValue(2,1), grid.getCellValue(2,2), ))
    return


print("Noughts and Crosses")
while(True):
    usr = str(input("1. Host a game.\n2. Connect and play.\n3. Exit.\n"))
    #the host will be user 1 and will take the first turn
    if(usr == '1'):
        print("Waiting for connection...")
        network.host()
        break
    if(usr == '2'):
        network.connect()
        break
    if(usr == '3'):
        sys.exit()


if(usr == '1'):
    #send name first, after waiting for 1 second to make sure other client is listening
    name = input("Enter your name: ")
    network.send(name)
    #listen for opponent to send name
    opponent_name = network.receive()
    print("You are playing against %s." % opponent_name)
    print("%s, you are crosses, you go first!" % name)
    #will turn is true, will take the next turn
    turn = True
    #the character that will be set on the grid
    char = 'x'
    other_char = 'o'


if(usr == '2'):
    #wait for opponent to send name
    opponent_name = network.receive()
    print("You are playing against %s." % opponent_name)
    #send name
    name = input("Enter your name: ")
    network.send(name)
    print("%s, you are noughts, you go second." % name)
    turn = False
    char = 'o'
    other_char = 'x'

#game loop
while(True):
    draw_grid(grid)
    if(turn):
        print("It is your turn!")
        while(True):
            #input the x and y coordinate of cell
            x_choice = input("Enter x position.")
            #check range
            if(int(x_choice) > 2):
                print("Enter a number below 3.")
                continue
            y_choice = input("Enter y position.")
            if(int(y_choice) > 2):
                print("Enter a number below 3.")
                continue
            if(grid.getCellValue(int(y_choice), int(x_choice)) != ' '):
                #check if cell is occupied
                print("Cell is already occupied.")
            else:
                #set value of the cell
                grid.setCellValue(int(y_choice), int(x_choice), char)
                #send cell coordinates to other player
                coord = [y_choice, x_choice]
                coord = ''.join(coord)
                network.send(coord)
                break

    else:
        print("It is %s's turn." % opponent_name)
        #recieve string from other client containing the coordinates
        coord = network.receive()
        grid.setCellValue(int(coord[0]), int(coord[1]), other_char)

    #check if you win
    if(check_win(grid, char)):
        draw_grid(grid)
        #if your turn, you win!
        print("You win!\n\n")
        network.close()
        input("Press enter to continue.")
        sys.exit()
    #check if other player wins
    if(check_win(grid, other_char)):
        draw_grid(grid)
        print("%s wins.\n\n" % opponent_name)
        network.close()
        input("Press enter to continue.")
        sys.exit()
    #check if the board is full => stalemate
    if(check_full(grid)):
        draw_grid(grid)
        print("Stalemate, nobody wins.")
        network.close()
        input("Press enter to continue.")
        sys.exit()
    #next player's turn
    turn = not turn
