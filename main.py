import os
import shutil
import time
import multiprocessing

from requests import get

from chess import *
from battleships import *
from noughtsandcrosses import *
from chat import *

network = Network_sockets()


def clear():
    """ Clears the screen based upon the type of operating system """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    return


def typewriter(message):
    """ A display function. Writes each character with a delay"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    return


def main():
    """ Runs the main program. """
    width = (shutil.get_terminal_size())[0]
    clear()

    print("Network Game Symposium".center(width))
    print("\n\n")

    # Main program loop.
    time.sleep(1)
    while True is True:
        usr = 0
        turn = None
        netName = None
        game = None
        gameChoice = None
        displayOpponentCommands = None
        localName = None
        opp_ip_addr = None

        while True is True:
            # Input menu loop
            usr = input("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: ")
            if usr == "1":
                gameChoice = "0"
                while gameChoice < "1" or gameChoice > "4":
                    gameChoice = input("\n\n1. Chess.\n2. Battleships."
                                       + "\n3. Noughts and Crosses.\n4. Return to homepage.\n\nEnter your choice: ")

                if gameChoice == "1":
                    game = Chess()
                    displayOpponentCommands = 1
                elif gameChoice == "2":
                    game = Battleships(1)
                    displayOpponentCommands = 0
                elif gameChoice == "3":
                    game = NoughtsAndCrosses()
                    displayOpponentCommands = 1
                elif gameChoice == "4":
                    clear()
                    continue
                else:
                    print("Please enter one of the above options..")
                    time.sleep(3)
                    clear()
                    continue
                # Create network connection
                ip_addr = get("https://api.ipify.org").text
                print("Your public IP address is: ", ip_addr)
                time.sleep(1)
                typewriter("Waiting for a connection...\n")
                network.host()
                opp_ip_addr = network.receive()
                break

            elif usr == "2":
                opp_ip_addr = input("Enter the IP address: ")
                ip_addr = get("https://api.ipify.org").text
                network.connect(opp_ip_addr)
                network.send(ip_addr)
                break

            elif usr == "3":
                sys.exit()

            else:
                print("Please enter one of the above options..")
                time.sleep(3)
                clear()
                continue

        if usr == "1":
            # Player 1 (Player making connection)
            turn = True

            network.send(gameChoice)

            localName = str(input("Enter your name: "))
            time.sleep(0.1)
            network.send(localName)
            netName = network.receive()
            clear()
            try:
                if int(network.receive()):
                    input("Press ENTER to continue ")

                else:
                    print("\nWaiting for " + netName + "..")
                    if int(network.receive()):
                        print("\nOk, we're done waiting.")
                        input("Press ENTER to continue ")

            except ValueError:
                input("Press ENTER to continue ")

        elif usr == "2":
            # Player 2 (Connecting Player)
            turn = False

            gameChoice = network.receive()
            if gameChoice == "1":
                game = Chess()
                displayOpponentCommands = 1
            elif gameChoice == "2":
                game = Battleships(2)
                displayOpponentCommands = 0
            else:
                game = NoughtsAndCrosses()
                displayOpponentCommands = 1

            localName = str(input("Enter your name: "))
            netName = network.receive()
            time.sleep(0.1)
            network.send(localName)
            time.sleep(0.1)
            network.send(0)
            clear()
            time.sleep(0.1)
            network.send(1)
            input("Press ENTER to continue ")

        print("Opening chat...")
        # open the chat window
        chat = multiprocessing.Process(target=open_chat, args=(localName, usr, opp_ip_addr))
        chat.start()

        # Game Explanations
        if gameChoice == "1":
            print("Welcome to Chess. Enter 'r' to resign, 'cl' and 'cr' to castle left or right (respectively) or a",
                  "set of co-ordinates in the form 'a1a1' to move a piece.")
            game.printBoard()
        elif gameChoice == "2":
            print("Welcome to Battleships. Enter in the format 'row, column, orientation' to place your ships.",
                  "To strike a ship, enter in the format 'row, column'. You can enter 'r' to resign at any time.")
        else:
            print("Welcome to Noughts And Crosses. Enter in the format 'x y' to place a mark at those coordinates.",
                  "x and y must be an integer in the range (0-2).")

        # Game play loop
        gameState = 0
        while gameState != -1:
            if turn is True:
                gameState = 0
                while gameState == 0:
                    userInput = input("\nIt's your turn!\nEnter your input: ")
                    print("\n")
                    network.send(userInput)
                    gameState = game.inputToGame(userInput)
                turn = False
            else:
                gameState = 0
                while gameState == 0:
                    print("\nWaiting for %s to play..." % netName)
                    userInput = network.receive()
                    if displayOpponentCommands == 1:
                        print("%s tries: %s\n\n" % (netName, userInput))
                    else:
                        print("%s entered a command" % netName)
                    gameState = game.inputToGame(userInput)

                    # Used for debug
                    # print(gameState)
                turn = True

        network.close()
        input("Press ENTER to Exit")
        chat.terminate()
        sys.exit()


if __name__ == "__main__":
    main()
