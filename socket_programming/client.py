import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
SERVER_IP = "10.209.67.140"
ADDR = (SERVER_IP,PORT)

client_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_soc.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = str(len(message)).encode(FORMAT)
    padded_msg_length = msg_length + (b' '*(HEADER-len(msg_length)))
    client_soc.send(padded_msg_length)
    client_soc.send(message)
    print(client_soc.recv(2048).decode(FORMAT))

send("HELLO WORLD!")
input()
send("This is client")

send(DISCONNECT_MSG)