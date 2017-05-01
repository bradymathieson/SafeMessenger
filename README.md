# SafeMessenger
A cryptographically safe messenger for non-corruptible communication among different computers.

## How to Run
This version runs on localhost, so you can only communicate between two terminal windows on the same machine (or, rather, with the same IP address). **This will be updated in the next version of this messenger with a web client.**

To run, simply clone the repository to your computer, navigate into the directory, and run `python chat.py`. Then, enter a port number for the respective window, and the port number to match the other window you wish to communicate with. If any ports are taken, you will receive an error message **but otherwise the program will continue running incorrectly**, so you must quit it manually. This should be updated in the future.

## Needed Libraries
To run the SafeMessenger, the following libraries must be installed:
- socket
- sys
- threading

**As of this posting, all these libraries come pre-installed in Python 2.7.**
