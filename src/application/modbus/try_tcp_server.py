import socket

# Configuración del servidor
host = '127.0.0.1'  # Puedes cambiar esto a la dirección IP de tu máquina
port = 8080

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y puerto especificados
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(5)

print(f"Servidor TCP escuchando en {host}:{port}")

while True:
    # Esperar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    # Enviar una respuesta al cliente
    response = "¡Hola desde el servidor!"
    client_socket.send(response.encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()
