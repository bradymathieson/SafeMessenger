import socket
import sys
import threading
from debug import *
import params

'''
socketing.py is a collection of functions used to facilitate errors associated with
the use of sockets. Networking is hard, so use these to make your job easier!

In summary, these functions will be used by the listener:
- listening_thread()
- create_socket()
- bind_socket()
- begin_accepting_connections()
- receive_data()

and these functions will be used by the sender:
- sending_thread()
- create_socket()
- connect_to_socket()
'''

# Starts a listening thread, and then returns.
def start_listening():
    try:
        listener = threading.Thread(target=listening_thread)
        listener.start()
    except:
        raise Exception("Listening thread could not be established")

# Starts a sending thread, and then returns.
def start_sending():
    try:
        sender = threading.Thread(target=sending_thread)
        sender.start()
    except:
        raise Exception("Sending thread could not be established")

'''
The listening thread does the following:
1) Creates a socket to listen on
2) Starts listening, with NUM_LISTENERS allowed to connect to this socket
3) Starts server, which runs infinitely
    a) Blocks while waiting to accept a connection
    b) Receives the data in the socket
    c) If receives a quit instruction from the client, terminates listening thread
'''
def listening_thread():
    print_message_debug("Entered listening thread")

    # Attempt to create socket and bind server to it.
    # Terminate if failed.
    try:
        s = create_socket()
        bind_socket(s)
    except Exception as e:
        print e
        return

    s.listen(params.NUM_LISTENERS)

    while True:
        client_socket = begin_accepting_connections(s)
        data = receive_data(s, client_socket)
        if data == "\q":
            print_message("[The other person has logged off. Enter '\q' to end this chat.]")
            client_socket.close()
            s.close()
            return
        else:
            print "Received: " + data

        client_socket.close()

'''
The sending thread does the following:
1) Starts server, which runs infinitely
    a) Blocks while waiting to receive text input from user
    b) Creates a socket to send the message on
    c) Connects to listening socket on other end which will receive message
    d) If message is appropriate length, sends the message to listening socket
       on other end.
    e) Closes socket, and terminates thread if a quit request is sent
'''
def sending_thread():
    print_message_debug("Entered sending thread")

    while True:
        x = raw_input()

        # Attempt to create a socket and connect to other socket.
        # Terminate if failed.
        try:
            s = create_socket()
            connect_to_socket(s)
        except Exception as e:
            print e
            return

        if sys.getsizeof(x) <= params.MAX_SEND_SIZE:
            s.sendall(x)
        else:
            print_message("Message too long, cannot send")

        s.close()

        if x == '\q':
            return

# Connects to 8.8.8.8 (Google DNS) in order to find the local IP address.
# Makes a temporary socket to achieve this.
def get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# Creates a socket using AF_INET, SOCK_STREAM (TCP) protocol
def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print_message_debug("Socket initialized")
        return s
    except socket.error, msg:
        raise Exception("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])

# Bind socket to a particular hostname/port number. Used by listening thread.
def bind_socket(s):
    try:
        s.bind((params.HOST, params.PORT))
        print_message_debug("Socket bind complete")
    except socket.error , msg:
        raise Exception("Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])

# Connect socket to external hostname/port number. Used by sending thread.
def connect_to_socket(s):
    try:
        s.connect((params.HOST, params.OTHER_PORT))
        print_message_debug("Socket connection complete")
    except socket.error , msg:
        raise Exception("Connection failed. Error Code : " + str(msg[0]) + " Message " + msg[1])

# Blocks until we have established an incoming connection. Used by listening thread.
def begin_accepting_connections(s):
    conn, addr = s.accept()
    print_message_debug("Receiving connection established")
    return conn

# Receives and returns data from the client. Used by listening thread.
# Max recv size is params.MAX_SEND_SIZE bytes (but remember sockets... could be more, could be less!)
def receive_data(s, conn):
    data = conn.recv(params.MAX_SEND_SIZE)
    return data
