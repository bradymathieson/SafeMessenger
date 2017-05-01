# Refers to other Python files in the same directory
from debug import *
from socketing import *
import params

'''
Potential reaches:
- cryptography
- message security (header messages)
- group chat!
'''

def main():
    print_message("[Enter port number]")
    params.PORT = int(raw_input())
    start_listening()
    print_message("[Enter other port number]")
    params.OTHER_PORT = int(raw_input())
    start_sending()
    print_message("----------")

if __name__ == '__main__':
    main()
