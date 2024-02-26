# from conpot.protocols.modbus.modbus_server import ModbusServer
# import os

# # Obtener la ruta al directorio actual del script
# my_dir = os.path.dirname(os.path.realpath(__file__))

# # Construir la ruta completa al archivo hola.xml

# template_file = os.path.join(my_dir, '..', 'configuration', 'template_modbus.xml')

# # Parámetros de inicio del servidor Modbus
# host = "127.0.0.1"
# port = 5020

# # Crear una instancia del servidor Modbus
# print("+++++++++++++++++++++++++++++++++++++")
# modbus_server = ModbusServer(template_file, None, None)
# print("+++++++++++++++++++++++++++++++++++++")

# # Iniciar el servidor en el host y puerto especificados
# print("+++++++++++++++++++++++++++++++++++++")
# modbus_server.start(host, port)
# print("+++++++++++++++++++++++++++++++++++++")
# print("Modbus Server started on port:"+str(port)+" and IP: "+host+"")


#pip install pyModbusTCP

import socket

from pyModbusTCP.server import ModbusServer

server_ip_address = "127.0.0.1"
server_port = 5002

server = ModbusServer(server_ip_address, server_port, no_block=True)

try:
    server.start()
    print("[+] Server is working on: IP: " + server_ip_address + " and PORT:" + str(server_port) + "")
    print("[+] Type 'quit' to stop the server.")

    while True:
        # Check for new connections
        addr = server.get_connection()
        if addr:
            print(f"[+] New connection from {addr}")

        # Check for user input to stop the server
        user_input = input()
        if user_input.lower() == "quit":
            break

finally:
    server.stop()
    print("[-] Server stopped.")
