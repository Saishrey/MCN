import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    msg = input("Enter message: ")
    server.send(bytes(msg, "utf-8"))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")