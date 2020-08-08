import socket
import sys


# Creation of socket. we are just Creating the socket without actually assigning of the port.
# global ---> global variables

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error:" + str(msg))


# here no host name because this is server side socket. we dont connect too any clients. client connect to server
# binding socket to port. Binding Socket = Assigning port to created socket using bind()

def socket_binding():
    try:

        print("Binding the socket to the port:" + str(port))
        s.bind((host, port))
        s.listen(10)
    except socket.error as msg:
        print("Socket Binding failed : " + str(msg) + "\n" + "Retrying")
        socket_binding()

# Accepting the connection

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established |" + "IP: " + address[0] + " |port: " + str(address[1]))
    send_commands(conn)
    # conn.close()


def send_commands(conn):
    print("Send commands \n")
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024), "utf-8")
            print(client_responce, end="")

socket_create()
socket_binding()
socket_accept()
