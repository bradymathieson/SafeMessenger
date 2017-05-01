import threading

# A lock so we're not print all over each other
PRINT_LOCK = threading.Lock()

# Debug mode
debug = True

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
