import socket
import threading

HOST = '127.0.0.1'
PORT = 7000
MAX_CONNECT_NUMBER = 5

def new_client(connect, addr):
    print('connected by ' + str(addr))

    while True:
        indata = connect.recv(1024)
        if len(indata) == 0: # connection closed
            connect.close()
            print('client closed connection.')
            break
        print('recv: ' + indata.decode())

        outdata = 'echo ' + indata.decode()
        connect.send(outdata.encode())
    connect.close()
    print("close it")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(MAX_CONNECT_NUMBER)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')


while True:
    conn, addr = s.accept()
    threading.Thread(target = new_client, args=(conn,addr,)).start()
    
    
