import socket
import sys
import threading

'''
Potential reaches:
- cryptography
- message security (header messages)
'''

# Constants for this server
HOST = 'localhost'
PORT = 0
OTHER_PORT = 0
MAX_SEND_SIZE = 1024

# A lock so we're not print all over each other
PRINT_LOCK = threading.Lock()

# Debug mode
debug = False

def main():
    global PORT, OTHER_PORT
    print_message("Enter port number: ")
    PORT = int(raw_input())
    start_listening()
    print_message("Enter other port number: ")
    OTHER_PORT = int(raw_input())
    start_sending()

def start_listening():
    try:
        listener = threading.Thread(target=listening_thread)
        listener.start()
    except:
        print_message_debug("Listening thread could not be established")
        sys.exit()

def start_sending():
    try:
        sender = threading.Thread(target=sending_thread)
        sender.start()
    except:
        print_message_debug("Sending thread could not be established")
        sys.exit()

def listening_thread():
    print_message_debug("Entered listening thread")

    s = create_socket()
    bind_socket(s)

    conn = begin_accepting_connections(s)
    receive_data(s, conn)
    # while 1:
    #     receive_data(s, conn)

def sending_thread():
    print_message_debug("Entered sending thread")

    s = create_socket()
    connect_to_socket(s)

    x = raw_input()
    # if sizeof(x) <= MAX_SEND_SIZE:
    s.sendall(x)

def create_socket():
    # Initialize socket using AF_INET, SOCK_STREAM (TCP) protocol
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print_message_debug("Socket initialized")
        return s
    except socket.error, msg:
        print_message_debug('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
        sys.exit()

def bind_socket(s):
    # Bind socket to a particular hostname/port number
    try:
        s.bind((HOST, PORT))
        print_message_debug("Socket bind complete")
    except socket.error , msg:
        print_message_debug('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

def connect_to_socket(s):
    try:
        s.connect((HOST,OTHER_PORT))
        print_message_debug("Socket connection complete")
    except socket.error , msg:
        print_message_debug('Connection failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

def begin_accepting_connections(s):
    s.listen(1)

    # Blocks until we have established a connection
    conn, addr = s.accept()

    print_message_debug("Receiving connection established")
    return conn

def receive_data(s, conn):

    # Max recv size is MAX_SEND_SIZE bytes (but remember sockets... could be more, could be less!)
    data = conn.recv(MAX_SEND_SIZE)
    print_message("Received: " + data)

def print_message(msg):
    PRINT_LOCK.acquire()
    print msg
    PRINT_LOCK.release()

def print_message_debug(msg):
    global debug
    if debug:
        PRINT_LOCK.acquire()
        print msg
        PRINT_LOCK.release()

if __name__ == '__main__':
    main()
