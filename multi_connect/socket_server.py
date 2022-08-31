import socket
import threading

HOST = '127.0.0.1'
PORT = 7000
MAX_CONNECT_NUMBER = 5


def new_client(connect, addr,index):
    print('connected by ' + str(addr))

    while True:
        indata = connect[index].recv(1024)
        if len(indata) == 0: # connection closed
            connect[index].close()
            print('client closed connection.')
            break
        print('recv: ' + indata.decode())

        outdata = 'echo ' + indata.decode()
        connect[index].send(outdata.encode())
    connect[index].close()
    print("close it")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(MAX_CONNECT_NUMBER)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

connect = []
index = 0
while True:
    conn, addr = s.accept()
    connect.append(conn)
    threading.Thread(target = new_client, args=(connect,addr,index,)).start()
    index = index+1
    
