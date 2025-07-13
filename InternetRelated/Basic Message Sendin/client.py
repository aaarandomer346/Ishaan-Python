import socket
from threading import Event, Thread

HEADER = 64
PORT = 7500
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.29.94" # specifies the server we want to connect to
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) # connects the client to the server

condition = Event()

def send(msg):
    message = msg.encode(FORMAT) # encodes the message
    msg_length = len(message) # gets the length of the message
    send_length = str(msg_length).encode(FORMAT) # encodes the message
    send_length += b' ' * (HEADER - len(send_length))
    # gets length, subtracts from the HEADER, adds the remaing in the form of blank spaces
    client.send(send_length)
    client.send(message)

def checkForMessages():
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if message:
                print(message)
        except:
            break

def continueChecking():
    while not condition.is_set():
        checkForMessages()

msg = "USERNAME: " + input("Whats your username? ")
send(msg)

Thread(target=continueChecking, daemon=True).start()

msg = "DESTINATION: " + input("Who are you sending to? ")
send(msg)


msg = "MESSAGE: " + input("What do you want to send? ")
send(msg)
send(DISCONNECT_MESSAGE)
condition.set()