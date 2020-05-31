import socket
# Use "pip install pycryptodome" to install the required libraries
from Crypto.Cipher import AES


class Network_sockets:

    # random unique default password, obtained from
    # https://passwordsgenerator.net/
    password = "n2d=&3@X*AGLKrkmsuGKcT3PfyBUendb"

    # Sets the password with input from the user
    def setpassword(self, pwd=None):
        if (not pwd):
            return 0
        elif (len(pwd) > 32):
            return -1
        else:
            # pads the password with 0's to conform to AES-256 standards
            self.password = pwd.zfill(32)
            return 0

    # Implementing symmetric encryption with both parties having to use the
    # same key and initalization vector
    def do_encrypt(self, message):
        # Creates an object (cipher) to encrypt the message
        obj = AES.new(
            self.password.encode("utf8"),
            AES.MODE_CFB,
            "2tacPDrETQxPWg?f".encode("utf8"))
        # Converts the string to binary to be encrypted
        message = message.encode("utf8")
        # Encrypts the message using the unique cipher
        cipherText = obj.encrypt(message)
        return cipherText

    def do_decrypt(self, cipherText):
        # Creates an object (cipher) to decrypt the message
        obj2 = AES.new(
            self.password.encode("utf8"),
            AES.MODE_CFB,
            "2tacPDrETQxPWg?f".encode("utf8"))
        # Converts the string to binary to be decrypted
        message = obj2.decrypt(cipherText)
        # Decrypts the message using the unique cipher
        message = message.decode("utf8")
        return message

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
        msg = self.do_encrypt(str(msg))
        if self.hosting:
            self.conn.send(msg)
        else:
            self.sock.send(msg)

    def receive(self):
        # Wait for the return string
        if self.hosting:
            return self.do_decrypt(self.conn.recv(1024))
        return self.do_decrypt(self.sock.recv(1024))

    def close(self):
        # Close connection
        self.sock.close()
