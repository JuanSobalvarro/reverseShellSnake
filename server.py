#!/usr/bin/python3
from operations.serverOp.server import Server

# IP_ADDR = '172.18.18.47'
# IP_ADDR = '172.18.6.66'
IP_ADDR = '192.168.1.25'
PORT = 6969

def main():
    server = Server(IP_ADDR, PORT)
    server.runserver()

if __name__ == '__main__':

    main()
