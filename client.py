from operations.clientOp.client import Client
import sys

# IP_ADDR = '172.18.18.47'
IP_ADDR = '172.18.6.66'
# IP_ADDR = '192.168.1.25'
PORT = 6969

def main():
    while True:
        client = Client(IP_ADDR, PORT)
        client.connect_to_host()

        client.run_client()


if __name__ == "__main__":
    main()