# from conpot.protocols.modbus.modbus_server import ModbusServer
# import os

# # 获取当前脚本所在的目录路径
# my_dir = os.path.dirname(os.path.realpath(__file__))

# # 构建完整的模板文件路径

# template_file = os.path.join(my_dir, '..', 'configuration', 'template_modbus.xml')

# # Modbus服务器的启动参数
# host = "127.0.0.1"
# port = 5020

# # 创建Modbus服务器实例
# print("+++++++++++++++++++++++++++++++++++++")
# modbus_server = ModbusServer(template_file, None, None)
# print("+++++++++++++++++++++++++++++++++++++")

# # 在指定的主机和端口上启动服务器
# print("+++++++++++++++++++++++++++++++++++++")
# modbus_server.start(host, port)
# print("+++++++++++++++++++++++++++++++++++++")
# print("Modbus Server started on port:"+str(port)+" and IP: "+host+"")


#pip install pyModbusTCP

import socket

from pyModbusTCP.server import ModbusServer

server_ip_address = "127.0.0.1"
server_port = 502

server = ModbusServer(server_ip_address, server_port, no_block=True)

try:
    server.start()
    print("[+] Server is working on: IP: " + server_ip_address + " and PORT:" + str(server_port) + "")
    print("[+] Type 'quit' to stop the server.")

    while True:
        # 检查新连接
        addr = server.get_connection()
        if addr:
            print(f"[+] New connection from {addr}")

        # 检查用户停止服务端的命令
        user_input = input()
        if user_input.lower() == "quit":
            break

finally:
    server.stop()
    print("[-] Server stopped.")
