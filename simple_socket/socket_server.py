import socket
import sys
HOST = '127.0.0.1'
PORT = 7000
MAX_CONNECT_NUMBER = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#參數1
#socket.AF_INET	於伺服器與伺服器之間進行串接
#socket.AF_INET6	使用IPv6於伺服器與伺服器之間進行串接
#參數2 UDP或是TCP

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#socket.SOL_SOCKET Socket選項的基本層級，用於指定要設置或獲取的Socket選項的範圍或類型，這裡選用的是socket.SO_REUSEADDR
#SO_REUSEADDR選項來設置地址重用
#1表示地址重用打開
#Socket地址重用在以下情況下非常有用：

#程序終止後立即重啟服務器，而不需要等待時間段的結束。
#網絡故障或意外斷開後，重新建立連接時能夠快速重用之前的本地地址。

#SOL_SOCKET的介紹 https://learn.microsoft.com/zh-tw/windows/win32/winsock/sol-socket-socket-options

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
