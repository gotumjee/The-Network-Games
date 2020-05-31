import os
import shutil
import time
import multiprocessing
import requests

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


def typewriter(message, speed):
    """ A display function. Writes each character with a delay"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == '\n':
            time.sleep(speed * 3)
        time.sleep(speed)
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
            typewriter("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: ", 0.01)
            usr = input()
            if usr == "1":
                gameChoice = "0"
                while gameChoice < "1" or gameChoice > "4":
                    typewriter("\n\n1. Chess.\n2. Battleships." +
                               "\n3. Noughts and Crosses.\n4. Return to homepage.\n\nEnter your choice: ", 0.01)
                    gameChoice = input()
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
                    typewriter("Please enter one of the above options..", 0.03)
                    time.sleep(3)
                    clear()
                    continue
                # Create network connection
                ip_addr = requests.get("https://api.ipify.org").text
                typewriter("Your public IP address is: " + ip_addr, 0.03)
                typewriter("\nWaiting for a connection... \n", 0.03)
                network.host()
                opp_ip_addr = network.receive()
                break

            elif usr == "2":
                typewriter("Enter the IP address: ", 0.03)
                opp_ip_addr = input()
                ip_addr = requests.get("https://api.ipify.org").text
                try:
                    network.connect(opp_ip_addr)
                    network.send(ip_addr)
                except KeyboardInterrupt:
                    return
                except ConnectionRefusedError:
                    typewriter(
                        "\nUnexpected error. Please check the IP address and try again.", 0.03)
                    time.sleep(2)
                    clear()
                    main()
                break

            elif usr == "3":
                sys.exit()

            else:
                typewriter("Please enter one of the above options..", 0.03)
                time.sleep(3)
                clear()
                continue

        if usr == "1":
            # Player 1 (Player making connection)
            turn = True

            network.send(gameChoice)

            while True is True:
                typewriter("Enter your name: ", 0.03)
                localName = input()
                if not localName:
                    typewriter(
                        "\nThat doesn't look like a name..\nTry again.\n\n", 0.03)
                    time.sleep(1)
                    continue
                else:
                    break
            time.sleep(0.1)
            network.send(localName)
            netName = network.receive()
            clear()

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

            while True is True:
                typewriter("Enter your name: ", 0.03)
                localName = str(input())
                if not localName:
                    typewriter("\nThat doesn't look like a name..\nTry again.\n\n", 0.03)
                    time.sleep(1)
                    continue
                else:
                    break
            netName = network.receive()
            time.sleep(0.1)
            network.send(localName)
            clear()

        typewriter("Opening chat...", 0.01)
        time.sleep(2)
        # open the chat window
        chat = multiprocessing.Process(
            target=open_chat, args=(
                localName, usr, opp_ip_addr))
        chat.start()
        clear()

        # Game Explanations
        if gameChoice == "1":
            typewriter("Welcome to Chess!", 0.03)
            time.sleep(1)
            typewriter(
                "\n\n\nEnter 'r' to resign, 'cl' and 'cr' to castle left or right (respectively) or a" +
                "set of co-ordinates in the form 'a1a1' to move a piece.\n",
                0.01)
            game.printBoard()
        elif gameChoice == "2":
            typewriter("Welcome to Battleships!", 0.03)
            time.sleep(1)
            typewriter(
                "\n\n\nEnter in the format 'row, column, orientation' to place your ships." +
                "\nTo strike a ship, enter in the format 'row, column'.\nYou can enter 'r' to resign at any time.\n",
                0.01)
        else:
            typewriter("Welcome to Noughts And Crosses!", 0.03)
            time.sleep(1)
            typewriter(
                "\n\n\nEnter in the format 'x y' to place a mark at those coordinates." +
                "x and y must be an integer in the range (0-2).\n",
                0.01)
        time.sleep(1)

        # Game play loop
        gameState = 0
        while gameState != -1:
            if turn is True:
                gameState = 0
                while gameState == 0:
                    typewriter("\nIt's your turn!\nEnter your input: ", 0.01)
                    userInput = input()
                    print("\n")
                    network.send(userInput)
                    gameState = game.inputToGame(userInput)
                turn = False
            else:
                gameState = 0
                while gameState == 0:
                    typewriter("\nWaiting for %s to play...\n" % netName, 0.01)
                    userInput = network.receive()
                    if displayOpponentCommands == 1:
                        typewriter(
                            "%s tries: %s\n\n" %
                            (netName, userInput), 0.01)
                    else:
                        typewriter("%s entered a command\n" % netName, 0.01)
                    gameState = game.inputToGame(userInput)

                    # Used for debug
                    # print(gameState)
                turn = True

        network.close()
        typewriter("\nPress ENTER to Exit\n", 0.01)
        input()
        chat.terminate()
        sys.exit()


if __name__ == "__main__":
    main()
