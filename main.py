from network import *
from chess import *
from requests import get
from time import sleep
import sys
import time
import os
import shutil

network = Network_sockets()


def clear():
    """ Clears the screen based upon the type of operating system """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    return


def typewriter(message):
    """ A display function. Writes each character with a """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    return


def main():
    width = (shutil.get_terminal_size())[0]
    clear()

    print("Network Game Symposium".center(width))
    print("\n\n")

    sleep(1)
    while True is True:
        usr = 0
        turn = None
        netName = None
        game = None

        while True is True:
            usr = input("1. Host a game.\n2. Connect and play.\n3. Exit.\n\nEnter your choice: ")
            if usr == "1":
                gameChoice = "0"
                while gameChoice < "1" or gameChoice > "3":
                    gameChoice = input("\n\n1. Chess.\n2. Battleships.\n3. Noughts and Crosses.\n\nEnter your choice: ")

                if gameChoice == 1:
                    game = Chess()
                elif gameChoice == 2:
                    pass
                else:
                    pass

                ip = get("https://api.ipify.org").text
                print("Your public IP address is: ", ip)
                sleep(1)
                typewriter("Waiting for a connection..")
                network.host()
                break

            elif usr == "2":
                network.connect()
                break

            elif usr == "3":
                sys.exit()

            else:
                print("Please enter one of the above options..")
                sleep(3)
                clear()
                continue

        if usr == "1":
            turn = True

            localName = str(input("Enter your name: "))
            sleep(0.1)
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
            turn = False

            localName = str(input("Enter your name: "))
            netName = network.receive()
            sleep(0.1)
            network.send(localName)
            sleep(0.1)
            network.send(0)
            clear()
            sleep(0.1)
            network.send(1)
            input("Press ENTER to continue ")

        gameState = None

        while gameState != -1:
            if turn is True:
                while gameState == 0:
                    userInput = input()
                    network.send(userInput)
                    gameState = game.inputToGame(userInput)
                turn = False
                gameState = None
            else:
                while gameState == 0:
                    print("Waiting for %s to play..." % netName)
                    userInput = network.receive()
                    print("%s tries: '%s'" % (netName, userInput))
                    gameState = game.inputToGame(userInput)
                turn = True
                gameState = None

        network.close()

if __name__ == "__main__":
    main()
