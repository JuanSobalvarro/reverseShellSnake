import socket


def retrieve_data(sock: socket.socket) -> bytes:
    all_data: bytes = b''
    while True:
        data = sock.recv(1024)
        if len(data) > 0:
            if b'done' in data:
                all_data += data.split(b'done')[0]
                break
            all_data += data
    return all_data