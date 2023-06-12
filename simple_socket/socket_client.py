import socket

HOST = '127.0.0.1'
PORT = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_UNIX	於本機端進行串接
#socket.AF_INET	於伺服器與伺服器之間進行串接
#socket.AF_INET6	使用IPv6於伺服器與伺服器之間進行串接
#socket.SOCK_STREAM	使用TCP提供可靠、雙向、串流的通信頻道
#socket.SOCK_DGRAM	使用UDP通用的免連線訊息交換通道
s.connect((HOST, PORT))

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
    
s.close()
