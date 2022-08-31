import socket

HOST = '127.0.0.1'
PORT = 7000

print("a")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("a")
s.connect((HOST, PORT))
print("a")
while True:
    outdata = input('please input message: ')
    print('send: ' + outdata)
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if len(indata) == 0: # connection closed
        s.close()
        print('server closed connection.')
        break
    print('recv: ' + indata.decode())
