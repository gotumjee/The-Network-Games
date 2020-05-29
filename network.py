import socket
from Crypto.Cipher import AES # Use "pip install pycryptodome" to install the required libraries


# Implementing symmetric encryption with both parties having to use the same key and initalization vector
def do_encrypt(message):
    # Creates an object (cipher) to encrypt the message
    obj = AES.new("#carperiemdabest".encode("utf8"), AES.MODE_CFB, "onlysometimestho".encode("utf8"))
    # Converts the string to binary to be encrypted
    message = message.encode("utf8")
    # Encrypts the message using the unique cipher
    cipherText = obj.encrypt(message) 
    return cipherText


def do_decrypt(cipherText):
    # Creates an object (cipher) to decrypt the message
    obj2 = AES.new("#carperiemdabest".encode("utf8"), AES.MODE_CFB, "onlysometimestho".encode("utf8"))
    # Converts the string to binary to be decrypted
    message = obj2.decrypt(cipherText)
    # Decrypts the message using the unique cipher
    message = message.decode("utf8") 
    return message


class Network_sockets:
    def __init__(self, port=6969):
        # Takes port number
        # Define port and use TCP
        # Use 6969 if no port number is given
        # If number too high, use default
        if port > 65535:
            port = 6969
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hosting = False
        self.conn = None
        self.addr = None

    def host(self):
        # Wait for incoming connection
        self.hosting = True
        self.sock.bind(('', self.port))
        self.sock.listen(5)
        self.conn, self.addr = self.sock.accept()

    def connect(self, ip_addr):
        self.sock.connect((ip_addr, self.port))

    def send(self, msg=''):
        # Takes a string then sends
        msg = do_encrypt(str(msg))
        if self.hosting:
            self.conn.send(msg)
        else:
            self.sock.send(msg)

    def receive(self):
        # Wait for the return string
        if self.hosting:
            return do_decrypt(self.conn.recv(1024))
        return do_decrypt(self.sock.recv(1024))

    def close(self):
        # Close connection
        self.sock.close()
