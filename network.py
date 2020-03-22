import socket
from Crypto.Cipher import AES #use "pip install pycryptodome" to install the required libraries

#implementing symmetric encryption with both parties having to use the same key and initalization vector
def do_encrypt(message):
    obj = AES.new("#carperiemdabest".encode("utf8"), AES.MODE_CFB, "onlysometimestho".encode("utf8")) #creates an object (cipher) to encrypt the message 
    message = message.encode("utf8") #converts the string to binary to be encrypted
    ciphertext = obj.encrypt(message) #encrypts the message using the unique cipher
    return ciphertext

def do_decrypt(ciphertext):
    obj2 = AES.new("#carperiemdabest".encode("utf8"), AES.MODE_CFB, "onlysometimestho".encode("utf8")) #creates an object (cipher) to decrypt the message
    message = obj2.decrypt(ciphertext) #converts the string to binary to be decrypted
    message = message.decode("utf8") #decrypts the message using the unique cipher
    return message

class Network_sockets:
    def __init__(self):
        #define port and use TCP
        self.port = 6969 #nice
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hosting = False

    def host(self):
        #wait for incoming connection
        self.hosting = True
        self.sock.bind(('',self.port))
        self.sock.listen(5)
        self.conn, self.addr = self.sock.accept()
        print("Received connection from ", self.addr)

    def connect(self):
        self.ip_addr = input("Enter the IP address: \n")
        self.sock.connect((self.ip_addr, self.port))

    def send(self, msg):
        #takes a string then sends
        msg=do_encrypt(msg)
        if(self.hosting):
            self.conn.send(msg)
        else:
            self.sock.send(msg)

    def receive(self):
        #wait for the return string
        print("\nWaiting for string..\n")
        if(self.hosting):
            return(do_decrypt(self.conn.recv(1024)))
        return(do_decrypt(self.sock.recv(1024)))

    def close(self):
        #close connection
        self.sock.close()
