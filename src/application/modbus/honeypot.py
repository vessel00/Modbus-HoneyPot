
import socket
import os
import logging
import threading
from modbus_functions import get_path_from_config_converted

ACTUAL_PATH = os.getcwd()
CONFIG_FILE = os.path.join(ACTUAL_PATH, "../../../", "config.json")
CONFIG_FILE = os.path.normpath(CONFIG_FILE)

from configuration.laod_config import cargar_seccion_modbus
modbus_dict = cargar_seccion_modbus(CONFIG_FILE)

host = modbus_dict['host']
port = modbus_dict['port']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=get_path_from_config_converted('log_file')
)

def handle_client(client_socket, client_address):
    print(f"Conexión entrante desde {client_address}")
    logging.info(f'[+] {client_address} New Connection.')

    # Enviar un mensaje de bienvenida al cliente
    WELCOME_MSG = modbus_dict['welcome_msg_client']
    client_socket.send(WELCOME_MSG.encode('utf-8'))

    # Mantener la conexión mientras el cliente no escriba 'exit'
    while True:
        # Recibir mensaje del cliente
        message = client_socket.recv(1024).decode('utf-8')
        print("EL MENSAJE INTRODUCIDO ES: " + message)
        EXIT_MSG = "exit"
        print(EXIT_MSG, message)

        if message == EXIT_MSG:
            print(f"Cliente {client_address} se desconectó.")
            break

        print(f"Mensaje de {client_address}: {message}")
        logging.info(f'[+] {client_address} CMD Received: {message}')

        # Enviar respuesta al cliente
        response = "Recibido desde el SERVER\n > "
        client_socket.send(response.encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Permitir hasta 5 conexiones en cola
server_socket.listen(5)

print(f"Servidor TCP escuchando en {host}:{port}")
logging.info(f"[+] ({host}:{port}) TCP SERVER LISTENING ...")

while True:
    # Esperar una conexión entrante
    client_socket, client_address = server_socket.accept()

    # Iniciar un hilo para manejar la conexión
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
