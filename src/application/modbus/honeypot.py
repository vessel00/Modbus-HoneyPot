import socket
import os
import logging
import threading
import sys
from modbus_functions import get_path_from_config_converted

ACTUAL_PATH = os.getcwd()
CONFIG_FILE = os.path.join(ACTUAL_PATH, "../../../", "config.json")
CONFIG_FILE = os.path.normpath(CONFIG_FILE)

src_path = os.path.normpath(os.path.join(ACTUAL_PATH, '..'))
sys.path.append(src_path)

from configuration.load_config import load_part_modbus
modbus_dict = load_part_modbus(CONFIG_FILE)

host = modbus_dict['host']
port = modbus_dict['port']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=get_path_from_config_converted('log_file')
)

def handle_client(client_socket, client_address):
    print(f"Incoming connection from {client_address}")
    logging.info(f'[+] {client_address} New Connection.')

    # 向客户端发送欢迎消息
    WELCOME_MSG = modbus_dict['welcome_msg_client']
    client_socket.send(WELCOME_MSG.encode('utf-8'))

    # 当客户端未写入 'exit' 时保持连接
    while True:
        try:
            # 接收客户端消息
            message = client_socket.recv(1024).decode('utf-8')
            print("The client input message is:" + message)
            EXIT_MSG = "exit"
            print(EXIT_MSG, message)

            if message == EXIT_MSG:
                print(f"Client {client_address} disconnected.")
                break

            print(f"Message from client {client_address}: {message}")
            logging.info(f'[+] {client_address} received command: {message}')

            # 向客户端发送回复消息
            response = "Server has received\n > "
            client_socket.send(response.encode('utf-8'))

        except UnicodeDecodeError as e:
            # print(f"错误解码信息: {e}")
            print(f"Client {client_address} disconnected.")
            logging.info(f'[-] {client_address} client disconnected')
            break

    # 关闭与客户端的连接
    client_socket.close()

# 创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# 允许最多5个等待连接
server_socket.listen()

print(f"TCP server is listening {host}:{port}")
logging.info(f"[+] ({host}:{port}) TCP server is listening ...")

try:
    while True:
        # 等待新的连接
        client_socket, client_address = server_socket.accept()

        # 启动一个线程来处理连接
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
except KeyboardInterrupt:
    print("The server has been stopped by the user.")
    logging.info("The server has been stopped by the user.")
    # 关闭服务器套接字
    server_socket.close()
    # 等待所有线程结束后再退出
    threading.Event().wait()