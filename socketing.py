import socket
import sys
import threading
from debug import *
import params

def start_listening():
    try:
        listener = threading.Thread(target=listening_thread)
        listener.start()
    except:
        print_message("Listening thread could not be established")
        sys.exit()

def start_sending():
    try:
        sender = threading.Thread(target=sending_thread)
        sender.start()
    except:
        print_message("Sending thread could not be established")
        sys.exit()

def listening_thread():
    print_message_debug("Entered listening thread")

    s = create_socket()
    bind_socket(s)

    s.listen(1)

    while True:
        client_socket = begin_accepting_connections(s)
        data = receive_data(s, client_socket)
        if data == "\q":
            print_message("[The other person has logged off. Enter '\q' to end this chat.]")
            s.close()
            return
        else:
            print "Received: " + data

        client_socket.close()

def sending_thread():
    print_message_debug("Entered sending thread")

    while True:
        x = raw_input()
        s = create_socket()
        connect_to_socket(s)
        if sys.getsizeof(x) <= params.MAX_SEND_SIZE:
            s.sendall(x)
        else:
            print_message("Message too long, cannot send")

        s.close()

        if x == '\q':
            return

def create_socket():
    # Initialize socket using AF_INET, SOCK_STREAM (TCP) protocol
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print_message_debug("Socket initialized")
        return s
    except socket.error, msg:
        print_message('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
        sys.exit()

def get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def bind_socket(s):
    # Bind socket to a particular hostname/port number
    try:
        s.bind((params.HOST, params.PORT))
        print_message_debug("Socket bind complete")
    except socket.error , msg:
        print_message('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

def connect_to_socket(s):
    try:
        s.connect((params.HOST, params.OTHER_PORT))
        print_message_debug("Socket connection complete")
    except socket.error , msg:
        print_message('Connection failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

def begin_accepting_connections(s):

    # Blocks until we have established a connection
    conn, addr = s.accept()

    print_message_debug("Receiving connection established")
    return conn

def receive_data(s, conn):

    # Max recv size is params.MAX_SEND_SIZE bytes (but remember sockets... could be more, could be less!)
    data = conn.recv(params.MAX_SEND_SIZE)
    return data
