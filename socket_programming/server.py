import socket 
import threading
HEADER = 64
SERVER_IP = socket.gethostbyname(socket.gethostname())#to get ip of our device
our_device_name = socket.gethostname()
PORT = 5050
print("server ip:",SERVER_IP)
print("serving device:",our_device_name)
ADDR = (SERVER_IP,PORT) 
FORMAT = "utf-8"

server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_soc.bind(ADDR)
#server.bind((SERVER_IP,PORT)) 

def handle_client(conn_soc,conn_addr):
    print("f[NEW CONNECTION]{conn_addr} connected")

    connected = True
    while connected:
        msg_length = conn_soc.recv(HEADER).decode(FORMAT)#since the length of the message is sent first
        if msg_length:#sometimes, especially at first the msg sent will be NONE, so we have to handle it
            msg_length = int(msg_length)
            msg = conn_soc.recv(msg_length).decode(FORMAT)#now the actual meassage is sent
            print(f"{conn_addr}:{msg}")
            if msg == "!DISCONNECT":
                conn_soc.send("DISCONNECTED!!".encode(FORMAT))
                connected = False
                continue
            conn_soc.send("MESSAGE SENT".encode(FORMAT))
    conn_soc.close()

def start():
    server_soc.listen()
    print(f"Server is listening on {SERVER_IP},{PORT}")
    while True:
        conn_soc , conn_addr = server_soc.accept()
        thread = threading.Thread(target=handle_client,args=(conn_soc,conn_addr))
        thread.start()
        print(f"[CURRENT ACTIVE CONNECTIONS]:{threading.active_count()-1}")

print("[STARTING] Server is starting....")
start()


