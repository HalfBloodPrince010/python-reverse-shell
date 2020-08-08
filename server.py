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


'''
s ---> socket
bind it ---> s.bind()
listen ---> s.listen()
Establishing the connection. In order to accept the connection the sockets must be listening.
First we Just create a socket and for that we bind the port. So thru that it(server side) will be listening.
Then we listen. That is waiting for client to request/establish a connection
We are accepting the connection. " s.accept() " .
It returns
conn --> connection itself
address -->It is a list.Information related to the client
address[0] = ip address(already a string)
address[1] = port address.


socket.accept()
Accept a connection. The socket must be bound to an address and listening for connections.
The return value is a pair(conn, address) where conn is a new socket object(connection) usable to send
and receive data on the connection, and address is the address bound to the socket on the
other end of the connection.(client side's).
input() ---> Takes command from the prompt
we don't stop after one command. So we put it inside while(1)
if cmd==quit. we close the connection. we close the socket and we quit. We quit using sys.exit()
This module provides a number of functions and variables that can be used to manipulate different
parts of the Python runtime environment.

For sending the data across the network we need to convert the data into bytes. That is done
  using encode(). We encode it and send it across the network. We are checking the length because
  to execute something if there is some cmd. No commands--> length=0
  Then we send the command thru using    send()

Then the client will execute the command and returns the result. we shd store it.
we use conn.recv(1024). Where,1024 is the buffer size and we have to convert it back to string
  using of the techniques(utf-8). We can use decode function also if needed.

Then we print it. Usually cursor moves to next line. we dont want that so use [end=""]
 for using end="" in python 2.X we use ---> from __future__ import print_function

'''







