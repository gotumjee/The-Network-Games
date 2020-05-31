from network import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
from time import sleep


class Chat:
    def __init__(self, root, name, usr, ip_addr):
        self.root = root
        self.name = name
        self.usr = int(usr)
        # Use different port to game
        self.network = Network_sockets(6970)
        if self.usr == 1:
            self.network.host()
        else:
            # Wait for 2 seconds to make sure the other client is listening
            sleep(2)
            self.network.connect(ip_addr)

        # Declare variable for text entry
        self.text_entry = StringVar(self.root)
        # Set window title
        self.root.title("Chat")
        # Text box for chat
        self.text = ScrolledText(self.root, bg="black", fg="white")
        self.text.grid(column=0, row=0, columnspan=2)
        # Declare text entry
        self.input = Entry(self.root, bg="black", fg="white", width=100, textvariable=self.text_entry)
        self.input.grid(column=0, row=1)
        # Declare send button
        self.button = Button(self.root, text="Send", bg="black", fg="white", command=self.send_message)
        self.button.grid(column=1, row=1)

        # Start receiver thread
        threading.Thread(target=self.recv_thread, daemon=True).start()

        # Bind enter to send function
        self.root.bind("<Return>", lambda x: self.send_message())

    def send_message(self):
        # Get text from text entry
        text = self.text_entry.get()
        # Clear entry box
        self.text_entry.set('')
        # Send using network module
        try:
            self.network.send("[{}]: {}\n".format(self.name, text))
            # Print message to text box
            self.text.insert(END, "[{}]: {}\n".format(self.name, text))
        except:
            self.text.insert(END, "Disconnected...\n")

    def recv_thread(self):
        # Listens for messages, then appends it to the text box
        try:
            while True:
                recv = self.network.receive()
                self.text.insert(END, recv)
        except:
            self.text.insert(END, "Disconnected...\n")


def open_chat(name, usr, ip_addr="127.0.0.1"):
    # Creates the chat window
    root = Tk()
    root.configure(bg="black")
    Chat(root, name, usr, ip_addr)
    root.mainloop()

# Testing Code
# localName = input("Enter your name: ")
# usr = input("1=host, 2=connect")

# Call this in main to open the window
# threading.Thread(target=open_chat, args=(localName, usr)).start()
