"""
演示Socket服务端开发
"""
import socket
# 创建Socket对象
socket_server = socket.socket()
# 绑定IP地址和端口
socket_server.bind(("localhost",8888))
# 监听端口
socket_server.listen(1)               # 整数参数表示接收连接的数量
# 等待客户端连接
# result = socket_server.accept()     # accept方法返回的是二元元祖(连接对象，客户端地址信息)
# conn = result[0]                    # 客户端和服务端的连接对象
# address = result[1]                 # 客户端的地址信息
conn,address = socket_server.accept()
# 注意：accept方法是阻塞的方法，等待客户端的连接，如果没有连接就卡在这一行不再向下执行
print(f"接受到了客户端的连接，客户端的信息是{address}")

while True:
    # 接收客户端信息 ,使用客户端和服务端的连接对象
    data = conn.recv(1024).decode("UTF-8")
    # recv -接受的参数是缓冲区的大小，一般1024即可
    # recv方法的返回值是一个字节数组也就是byte对象，可以通过decode方法使用utf-8编码将字节数组转换为字符串对象
    print(f"客户端发来的消息是：{data}")
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：")  # encode可以将字符串编码为字节数组对象
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socket_server.close()