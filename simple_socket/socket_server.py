import socket
import sys
HOST = '127.0.0.1'
PORT = 7000
MAX_CONNECT_NUMBER = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(MAX_CONNECT_NUMBER)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            #break
            sys.exit()
        print('recv: ' + indata.decode())

        outdata = 'echo ' + indata.decode()
        conn.send(outdata.encode())
