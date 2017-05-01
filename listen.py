import socket
import sys

# Constants for this server
HOST = 'localhost'
PORT = 1234

def main():
    s = create_socket()
    bind_socket(s)
    conn = begin_accepting_connections(s)
    while 1:
        receive_data(s, conn)

def create_socket():
    # Initialize socket using AF_INET, SOCK_STREAM (TCP) protocol
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket initialized"
        return s
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()

def bind_socket(s):
    # Bind socket to a particular hostname/port number
    try:
        s.bind((HOST, PORT))
        print "Socket bind complete"
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

def begin_accepting_connections(s):
    s.listen(1)

    # Blocks until we have established a connection
    conn, addr = s.accept()

    print "Connection established"
    return conn

def receive_data(s, conn):
    data = conn.recv(1024)
    print data

if __name__ == '__main__':
    main()
