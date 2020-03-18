import socket

class Network_sockets:
    def __init__(self):
        #define port and use TCP
        self.port = 6969
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hosting = False

    def host(self):
        #wait for incoming connection
        self.hosting = True
        self.sock.bind(('',self.port))
        self.sock.listen(5)
        self.conn, self.addr = self.sock.accept()
        print("Received connection from", self.addr)

    def connect(self):
        self.ip_addr = input("Enter the IP address\n")
        self.sock.connect((self.ip_addr, self.port))

    def send(self, msg):
        #takes a string then sends
        if(self.hosting):
            self.conn.send(msg.encode())
        else:
            self.sock.send(msg.encode())

    def receive(self):
        #wait for then return string
        print("Waiting for string")
        if(self.hosting):
            return(self.conn.recv(1024).decode())
        return(self.sock.recv(1024).decode())

    def close(self):
        #close connection
        self.sock.close()
