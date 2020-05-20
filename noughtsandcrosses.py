from network import *
from GridModule import *
import sys
from time import sleep

class NoughtsAndCrosses:
    def __init__(self):
        #initiate connection
        print("Noughts and Crosses")
        while(True):
            self.network = Network_sockets()
            self.grid = Grid(3, 3, ' ')

            self.usr = str(input("1. Host a game.\n2. Connect and play.\n3. Exit.\n"))
            #the host will be user 1 and will take the first turn
            if(self.usr == '1'):
                print("Waiting for connection...")
                self.network.host()
                break
            if(self.usr == '2'):
                self.network.connect()
                break
            if(self.usr == '3'):
                return -1

        #send names, one user must send their name first and the other will send theirs after recieving
        if(self.usr == '1'):
            #send name first, after waiting for 1 second to make sure other client is listening
            self.name = input("Enter your name: ")
            self.network.send(self.name)
            #listen for opponent to send name
            self.opponent_name = self.network.receive()
            print("You are playing against %s." % self.opponent_name)
            print("%s, you are crosses, you go first!" % self.name)
            #will turn is true, will take the next turn
            self.turn = True
            #the character that will be set on the grid
            self.char = 'x'
            self.other_char = 'o'


        if(self.usr == '2'):
            #wait for opponent to send name
            self.opponent_name = self.network.receive()
            print("You are playing against %s." % self.opponent_name)
            #send name
            self.name = input("Enter your name: ")
            self.network.send(self.name)
            print("%s, you are noughts, you go second." % self.name)
            self.turn = False
            self.char = 'o'
            self.other_char = 'x'

    def check_win(self, check):
        #check if victory conditions have been met
        #returns true or false
        #check rows
        for i in range(3):
            if(self.grid.getCellValue(0,i)==check and self.grid.getCellValue(1,i)==check and self.grid.getCellValue(2,i)==check):
                    return True
        #check columns
        for i in range(3):
            if(self.grid.getCellValue(i,0)==check and self.grid.getCellValue(i,1)==check and self.grid.getCellValue(i,2)==check):
                    return True
        #check diagonals
        if(self.grid.getCellValue(0,0)==check and self.grid.getCellValue(1,1)==check and self.grid.getCellValue(2,2)==check):
            return True
        if(self.grid.getCellValue(0,2)==check and self.grid.getCellValue(1,1)==check and self.grid.getCellValue(2,0)==check):
            return True
        return False

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
        return


    #game loop
    def game(self):
        while(True):
            self.draw_grid()
            if(self.turn):
                print("It is your turn!")
                while(True):
                    #input the x and y coordinate of cell
                    self.x_choice = input("Enter x position.")
                    #check range
                    if(int(self.x_choice) > 2):
                        print("Enter a number below 3.")
                        continue
                    self.y_choice = input("Enter y position.")
                    if(int(self.y_choice) > 2):
                        print("Enter a number below 3.")
                        continue
                    if(self.grid.getCellValue(int(self.y_choice), int(self.x_choice)) != ' '):
                        #check if cell is occupied
                        print("Cell is already occupied.")
                    else:
                        #set value of the cell
                        self.grid.setCellValue(int(self.y_choice), int(self.x_choice), self.char)
                        #send cell coordinates to other player
                        self.coord = [self.y_choice, self.x_choice]
                        self.coord = ''.join(self.coord)
                        self.network.send(self.coord)
                        break

            else:
                print("It is %s's turn." % self.opponent_name)
                #recieve string from other client containing the coordinates
                self.coord = self.network.receive()
                self.grid.setCellValue(int(self.coord[0]), int(self.coord[1]), self.other_char)

            #check if you win
            if(self.check_win(self.char)):
                self.draw_grid()
                #if your turn, you win!
                print("You win!\n\n")
                self.network.close()
                input("Press enter to continue.")
                sys.exit()
            #check if other player wins
            if(self.check_win(self.other_char)):
                self.draw_grid()
                print("%s wins.\n\n" % self.opponent_name)
                self.network.close()
                input("Press enter to continue.")
                return -1
            #check if the board is full => stalemate
            if(self.check_full()):
                self.draw_grid()
                print("Stalemate, nobody wins.")
                self.network.close()
                input("Press enter to continue.")
                return -1
            #next player's turn
            self.turn = not self.turn


#initiate class
noughts_and_crosses = NoughtsAndCrosses()
noughts_and_crosses.game()
