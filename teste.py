import socket
import threading

def handle_client(client_socket):
    # Lógica para lidar com as requisições do cliente
    request = client_socket.recv(1024)
    response = "Servidor recebeu a mensagem: " + request.decode('utf-8')
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Servidor iniciado e escutando na porta 8000.")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Cliente conectado:", client_address)

        # Iniciar uma nova thread para lidar com o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()