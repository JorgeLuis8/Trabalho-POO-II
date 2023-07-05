import socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print("Resposta do servidor:", response.decode('utf-8'))
    client_socket.close()

# Enviar uma mensagem para o servidor
send_message("Olá, servidor!")
