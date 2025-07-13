import socket
import threading

# full uppercase variables are constants

# using threading to allow multiple stuff to run at the same time
# a client isnt waiting for another client to communicate

# to send objects, google it. smth using pickels and jsons

HEADER = 64 # every single time, the first message needs to be this big in bytes
# before any message is sent, send a message with how many bytes the message will be
    # increase byte size if needed
# and then send the message
# increase if needed
PORT = 7500 # sets a port to communicate on
SERVER = socket.gethostbyname(socket.gethostname()) # gets the ip address of this computer
# change to the result of "my public ip address" to allow devices anywhere to connect
# we use the above since then it allows the servers to run on other devices
# if we dont use this, then we need to hard code the ip address of the device the server is running on
# and if your planning for the server to run on multiple other devices, this is the best for local
ADDR = (SERVER, PORT)
FORMAT = "utf-8" # english strings
DISCONNECT_MESSAGE = "!DISCONNECT" # set the disconnect message


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creates new socket, first arg is the family/catagory
# the first arg gives what type of addresses we are looking for
# second arg gives how we are sending data, most common
server.bind(ADDR) # binds the address

# for client to client:
# make a protocol where when the server recives the message, they also get the destination
# if the destination is valid, send it
# if not, respond back to client


################################################################################
################################################################################
# for chat application:
################################################################################
################################################################################

# https://docs.python.org/3/library/socket.html#other-functions
# socket.sendto(bytes, address)
# before allowing clients to use server ask them to give a username
# send the username to the server
# assosiate the address with the username
# when asking them who to send a message to, ask them first for a username to send to
# and then allow them to send a message
# if the username doesnt match any username in the list, return a message saying it doesn't


connectedIdentities = []

def handle_client(conn, addr):
    global connectedIdentities
    identity = ["", addr, conn]
    # runs for each client, runs in parallel
    print(f"[NEW CONNECTION] {addr} connected.")

    validDestination = False

    connected = True
    destination = ''

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # a "blocking" line of code, does not go forward until a message appears
        # wait till something is sent through the socket
        # first arg gives total number of bytes
        # .decode() decodes it from bytes to any format
        if msg_length: # if the msg is valid, sometimes on startup client sends empty msg
            msg_length = int(msg_length) # sets the length to an int
            msg = conn.recv(msg_length).decode(FORMAT) # waits to get the message with the length given

            if msg == DISCONNECT_MESSAGE: # if the disconnect message is recieved
                conn.send("CONNECTION TERMINATED".encode(FORMAT))
                connected = False # stop the while loop
            elif "USERNAME:" in msg:
                identity[0] = msg[10:]
                connectedIdentities.append(identity)
                print("Connected IDs:", connectedIdentities)
                conn.send("USERNAME RECIEVED".encode(FORMAT))
            elif "DESTINATION:" in msg:
                print(f"[{addr}] {msg}")
                msg = msg[13:]
                destination = msg
                for identityRecv in connectedIdentities:
                    if identityRecv[0] == msg:
                        validDestination = True
                        conn.send("VALID DESTINATION".encode(FORMAT))
                        break
                if validDestination != True:
                    conn.send("INVALID DESTINATION".encode(FORMAT))
            elif "MESSAGE:" in msg and validDestination == True:
                for whoRecvs in connectedIdentities:
                    if whoRecvs[0] == destination:
                        whoRecvs[2].send(f"[{identity[0]}] {msg}".encode(FORMAT))
            print(f"[{addr}] {msg}")


    conn.close() # closes the connection
    # this is important as if the client doesn't tell that they disconnected
    # they wouldn't be allowed to join later since, in the servers eyes, they are still connected

def start():
    server.listen() # listening to new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # will wait at this line until a new connection, "blocking" line
        # stores the IP along with the address in the form of a socket object
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # when a new connection occurs, start a new thread with the args given
        thread.start() # starts the thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # gives active amount of threads
        print(addr)

print("[STARTING] Server Is Starting...")
start()