from network import *

#this file is just an example of how the network stuff will be used
#one client will call host(), and the other will call connect()
#to send a string, one client must be listening using receive() and then the other calls send
#at the end, both clients should call close()

network = Network_sockets()

while(True):
    usr = input("Host (h) or connect (c)").lower()
    if(usr == 'h'):
        host_ip = socket.gethostbyname(socket.gethostname())
        print("IP Address: ", host_ip)
        i = False
        network.host()
        break
    elif(usr == 'c'):
        i = True
        network.connect()
        break

#the connecting client sends the first message

while(True):
    if(i == True):
        network.send(input(""))
    elif(i == False):
        print(network.receive())
    if(i):
        i = False
    else:
        i = True
