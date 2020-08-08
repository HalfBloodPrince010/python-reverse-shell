# python-reverse-shell
Implementation of Reverse Shell using Python 3 and the purpose of this project is to help troubleshoot remote systems. We can make the remote system connect to us with necessary permissions and making it possible for us to obtain the shell of those remote systems.

Client :

create a socket at this end and connect it to server's IP and Port using s.connect()
by passing a tuple of addresses as argument.

os module : provides a way of using 'OPERATING SYSTEM' dependent functionality.The functions
that the OS module provides allows you to interface
with the underlying operating system that Python is running on be that Windows,
Mac or Linux.

client side socket port number will be randomly assigned by the OS.
2^16-1 = 65535(including 0)

If it is 'cd' we ask the OS to change the directory. Because it doesnt give us any data it just changes
the directory

if length of the data(command received) is greater than 0 that means we have a command.
we create a subprocess and
" All the input and output to that are through standard stream(stdout,stdin,stderr) so we use PIPE"
// very very important

Then we use output in both bytes and string.
and we have to send in bytes + the path + >

If the len(data) is NOT greater than 0, then that if FAILS. 


Server:

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
