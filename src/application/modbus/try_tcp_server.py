import socket

host = '127.0.0.1'
port = 8080

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Permitir hasta 5 conexiones en cola
server_socket.listen(5)

print(f"Servidor TCP escuchando en {host}:{port}")

while True:
    # Esperar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    # Enviar un mensaje de bienvenida al cliente
    welcome_message = "¡WELCOME TO THE SERVER!.\n"
    client_socket.send(welcome_message.encode('utf-8'))

    # Mantener la conexión mientras el cliente no escriba 'exit'

    while True:
        # Recibir mensaje del cliente
        message = client_socket.recv(1024).decode('utf-8')

        if message.lower() == 'exit':
            print(f"Cliente {client_address} se desconectó.")
            break

        print(f"Mensaje de {client_address}: {message}")

        # Enviar respuesta al cliente
        response = input("Tu respuesta: ")
        client_socket.send(response.encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()
