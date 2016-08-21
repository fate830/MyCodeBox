import socket

M_HOST ="127.0.0.1"
M_PORT = 8099

client = socket.socket()
client.connect((M_HOST,M_PORT))

while True:
    client.sendall("adasdasdadasd".encode())          # 把命令发送给对端
    data=client.recv(1024)       # 把接收的数据定义为变量
    print (data.decode())              # 输出变量
s.close()                   # 关闭连接