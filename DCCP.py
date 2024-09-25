import socket

# Crear un socket DCCP
dccp_socket = socket.socket(socket.AF_INET, socket.SOCK_DCCP, socket.IPPROTO_DCCP)

# Asignar puerto y dirección
host = '127.0.0.1'  # Dirección local
port = 65432  # Puerto

# Enlazar el socket a una dirección y puerto
dccp_socket.bind((host, port))

# Escuchar conexiones entrantes
dccp_socket.listen(1)

print(f"Esperando conexiones en {host}:{port}...")

# Aceptar una conexión
conn, addr = dccp_socket.accept()
print(f"Conexión aceptada de {addr}")

# Recibir datos
data = conn.recv(1024)
print(f"Recibido: {data}")

# Enviar respuesta
conn.sendall(b'Hola desde el servidor DCCP')

# Cerrar la conexión
conn.close()
dccp_socket.close()
