import socket

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dirección del servidor
server_address = ('127.0.0.1', 65432)

# Enviar datos
sock.sendto(b'Hola, servidor', server_address)

# Recibir respuesta
data, server = sock.recvfrom(1024)
print(f"Recibido: {data}")

# Cerrar el socket
sock.close()
