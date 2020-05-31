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
        print(char, end='', flush=True)
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
            typewriter(
                "1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: ",
                0.01)
            usr = input()
            if usr == "1":
                while (1):
                    typewriter(
                        "Enter a password for the game (leave blank for no password): ", 0.01)
                    if(network.setpassword(input()) == -1):
                        typewriter(
                            "The password is too long..\nPlease try a shorter password.", 0.03)
                        time.sleep(3)
                        clear()
                        continue
                    typewriter("The password has been set!", 0.01)
                    time.sleep(2)
                    clear()
                    break

                gameChoice = "0"
                while (1):
                    typewriter(
                        "Which game would you like to play?\n\n1. Chess.\n2. Battleships." +
                        "\n3. Noughts and Crosses.\n4. Return to homepage.\n\nEnter your choice: ",
                        0.01)
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
                        main()
                        continue
                    else:
                        typewriter(
                            "Please enter one of the above options..", 0.03)
                        time.sleep(3)
                        clear()
                        continue
                    break
                # Create network connection
                try:
                    ip_addr = requests.get("https://api.ipify.org").text
                    typewriter("Your public IP address is: " + ip_addr, 0.03)
                except BaseException:
                    ip_addr = "127.0.0.1"
                    typewriter(
                        "Your public IP address is currently unknown..\nUsing localhost.", 0.03)

                typewriter("\nWaiting for a connection...", 0.03)
                network.host()
                while(1):
                    network.send(1)
                    try:
                        if(network.receive() == str(1)):
                            break
                    except UnicodeDecodeError:
                        continue
                opp_ip_addr = network.receive()
                clear()
                break

            elif usr == "2":
                typewriter(
                    "Enter the IP address (or enter \'r\' to go back): ", 0.03)
                opp_ip_addr = input()
                if(opp_ip_addr == 'r'):
                    main()
                try:
                    ip_addr = requests.get("https://api.ipify.org").text
                except BaseException:
                    ip_addr = "127.0.0.1"
                try:
                    network.connect(opp_ip_addr)
                except KeyboardInterrupt:
                    return
                except ConnectionRefusedError:
                    typewriter(
                        "\nUnexpected error. Please check the IP address and try again.", 0.03)
                    time.sleep(2)
                    main()
                while (1):
                    typewriter(
                        "Enter the password assigned by the host (leave blank if there's no password): ",
                        0.01)
                    network.setpassword(input())
                    network.send(1)
                    try:
                        if(network.receive() == str(1)):
                            typewriter("You have the right password!", 0.01)
                        else:
                            typewriter(
                                "\nThe password's incorrect..\nPlease double-check with the host.", 0.03)
                            time.sleep(3)
                            clear()
                            continue
                    except UnicodeDecodeError:
                        typewriter(
                            "\nThe password's incorrect..\nPlease double-check with the host.", 0.03)
                        time.sleep(3)
                        clear()
                        continue
                    network.send(ip_addr)
                    time.sleep(1)
                    clear()
                    break
                break

            elif usr == "3":
                exit()

            else:
                typewriter("Please enter one of the above options..", 0.03)
                time.sleep(3)
                main()
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
                    typewriter(
                        "\nThat doesn't look like a name..\nTry again.\n\n", 0.03)
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
            time.sleep(3)
            game.printBoard()
        elif gameChoice == "2":
            typewriter("Welcome to Battleships!", 0.03)
            time.sleep(1)
            typewriter(
                "\n\n\nEnter in the format 'row, column, orientation' to place your ships." +
                "\nOrientation options are \'h\'(Horizontal) or \'v\'(Vertical)." +
                "\nTo strike a ship, enter in the format 'row, column'.\nYou can enter 'r' to resign at any time.\n",
                0.01)
            time.sleep(3)
            game.display()
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
        time.sleep(3)
        clear()
        typewriter("\nPress ENTER to Exit\n", 0.01)
        input()
        chat.terminate()
        exit()


if __name__ == "__main__":
    main()
