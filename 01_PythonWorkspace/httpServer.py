import socket

M_HOST = "127.0.0.1"
M_PORT = 8099

server = socket.socket()
server.bind((M_HOST, M_PORT))
server.listen(1)

while True:
    conn,addr = server.accept()
    print("receive one client : %s \n" % 'addr')
    print(addr)
    while True:
        cdata = conn.recv(1024)
        print(cdata)
        strMsg = cdata.decode()
        print(strMsg)
        print(strMsg.split("\r\n"))
        conn.send('ok'.encode())
    conn.close()

