from network import *
import threading
import sys

class Chat:
    def __init__(self):
        #enter name and connect
        self.name = input("Enter your name: ")
        self.name_string = "[{}]: ".format(self.name)
        self.network = Network_sockets(6970)
        while True:
            self.usr = str(input("1. Host chat.\n2. Connect and chat.\n3. Exit.\n"))
            if(self.usr == '1'):
                print("Waiting for connection...")
                self.network.host()
                break
            if(self.usr == '2'):
                self.network.connect()
                break
                if(self.usr == '3'):
                    return

    def recv_thread(self):
        print("Connected to chat... (type \"Exit\" to exit.)")
        try:
            while True:
                print(self.network.receive())
        except:
            print("Disconnected, closing chat.")
            sys.exit()

    def chat_loop(self):
        t = threading.Thread(target = self.recv_thread, daemon = True)
        t.start()
        try:
            while True:
                self.text = input("\n")
                if(self.text == "Exit"):
                    self.network.close()
                    break
                else:
                    self.network.send(self.name_string + self.text)
        except:
            print("Disconnected, closing chat.")
            self.network.close()

chat = Chat()
chat.chat_loop()
