# SafeMessenger
A cryptographically safe messenger for non-corruptible communication among different computers.

## How to Run
This version runs on localhost, so you can only communicate between two terminal windows on the same machine (or, rather, with the same IP address). **This will be updated in the next version of this messenger with a web client.**

To run, simply clone the repository to your computer, navigate into the directory, and run `python chat.py`. Then, enter a port number for the respective window, and the port number to match the other window you wish to communicate with. If any ports are taken, you will receive an error message **but otherwise the program will continue running incorrectly**, so you must quit it manually. This should be updated in the future.

## How to Stop
When done communicating, **both parties must enter `\q` in the chat box.** Once one user enters `\q`, the other user will be prompted to do the same. Only once **both users** have entered `\q` will the program terminate for both ends.

## Needed Libraries
To run the SafeMessenger, the following libraries must be installed:
- socket
- sys
- threading

**As of this posting, all these libraries come pre-installed in Python 2.7.**

## To-Do List
In future versions, I will be working on:
- a web client to direct traffic to one unified IP address and allow communication between two users on different computers. This server will be run on Heroku and need error checks to make sure not to confuse messages when multiple chats are happening simultaneously (a method to make sure ports are taken by two clients at the same time).
- a more elegant way to end chats between two users.
- a clearer description of project requirements (still haven't figured out what students' responsibilities would be)
- reaches! (right now, thinking cryptography over the network, group chat, web interface, or safer communication with cleartext headers)

## Giving Credit Where Credit Is Due
This is a clear example of how EECS 482 (Introduction to Operating Systems) and 485 (Web Systems) at the University of Michigan have shaped me as a programmer. Eternally grateful for the staff and professors from both of these respective courses (in particular, Jason Flinn of 482 and Andrew DeOrio/Hosagrahar Jagadish of 485).
